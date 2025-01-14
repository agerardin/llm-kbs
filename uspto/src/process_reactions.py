
"""Process the first reaction in the USPTO dataset using a llm model with structured output."""

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from lxml import etree
import random
from langchain_core.prompts import ChatPromptTemplate
from generated import ReactionList
from config import INPDIR, OUTDIR
from parser_utils import count_elements, get_element_at_index
from llm_utils import generate_prompt_examples

from dotenv import find_dotenv, load_dotenv
import os
from langchain_openai import AzureChatOpenAI
load_dotenv(find_dotenv(), override=True)
llm = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_CHAT_GPT4O"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

# Create the parser with the namespaces configuration
# TODO still certain errors to need to be fixed
context = XmlContext(class_type="pydantic")
parser_config = ParserConfig(fail_on_unknown_properties=False, fail_on_unknown_attributes=False)
xml_parser = XmlParser(config=parser_config, context=context)
ser_config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(context=context, config=ser_config)

elt_count = count_elements(INPDIR / "pftaps19760106_wk01.xml")
ex_count = 5
exs = []

ex_idx = random.sample(range(elt_count), ex_count)
for idx in ex_idx:
    reaction = get_element_at_index(INPDIR / "pftaps19760106_wk01.xml", idx)
    if reaction:
        # Print the element as a string
        reaction_str = etree.tostring(reaction, pretty_print=True).decode()
        text = reaction.xpath(".//dl:source/dl:paragraphText/text()", namespaces={
            "dl": "http://bitbucket.org/dan2097"
        })[0]
        exs.append((text, reaction_str))

print(f"{exs} for ex at indices {ex_idx}")

ex_prompt = generate_prompt_examples(exs)
print(ex_prompt)

structured_llm = llm.with_structured_output(ReactionList.Reaction, include_raw=True)
# structured_llm = llm.with_structured_output(ReactionList.Reaction)

system = """You are a chemist. 
You are provide some textual description of a chemical reaction and you must 
extract as much relevant information as possible that fits in the output xml schema:
the reactants, the products, the conditions, the yield, the catalysts, the solvents, 
the steps taken, etc.
Try to extract the product amount if you can (value and units) and do the same for reactants.
Make sure to extract smile strings for the reactants and products if available.
For the reaction actions, make sure you extract a precise sequence of steps but
you must map each action to one of the allowed type in ReactionActionAction.
Try to make sure you capture a yield action if at all possible.
Make sure to breakdown the most important steps.
"""

system += f"""Here are some examples of chemical reactions and the corresponding xml-encoded output: {ex_prompt}"""

prompt = ChatPromptTemplate.from_messages([("system", system)])
few_shot_structured_llm = prompt | structured_llm

# Parse the XML file
with open(INPDIR / "pftaps19760106_wk01.xml", "rb") as file:
    ns = {} # ns will be populated by the parser
    reaction_list = xml_parser.parse(file, ReactionList, ns_map=ns)

# Process the parsed data
# ns = {"": "http://www.xml-cml.org/schema", "dl":"http://bitbucket.org/dan2097"}

for i, reaction in enumerate(reaction_list.reaction):
    text = reaction.source[0].paragraph_text[0]
    print(f"Processing reaction: {text}")
    resp = structured_llm.invoke(text, temperature=1)
    print("output: {}".format(resp))
    if resp['parsing_error']:
        raise ValueError(f"Failed to parse the input {i}: {resp['parsing_error']}")
    output_xml = serializer.render(resp['parsed'], ns_map=ns)
    print(output_xml)

    # Save the output XML to a file
    reaction_name = reaction.source[0].heading_text[0].replace(" ", "_")
    output_file_path = f"{reaction_name}.xml"
    with open(OUTDIR / "few_shots" / f"{ex_count}ex_{output_file_path}", "w") as output_file:
        print(f"Writing output to {output_file_path}")
        print(f"Content: {output_xml}")
        output_file.write(output_xml)

    exit(0)
