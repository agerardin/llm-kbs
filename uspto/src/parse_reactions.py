"""Test the generated xsdata model."""

from xsdata_pydantic.bindings import XmlParser as PydanticXmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from generated import ReactionList

# Create the parser with the namespaces configuration
config = ParserConfig(fail_on_unknown_properties=False, fail_on_unknown_attributes=False)
xml_parser = PydanticXmlParser(config=config)

# Parse the XML file
with open("/polus2/gerardinad/data/uspto/pftaps19760106_wk01.xml", "rb") as file:
    reaction_list = xml_parser.parse(file, ReactionList)

# Process the parsed data
for reaction in reaction_list.reaction:
    print(f"Processing reaction: {reaction}")
    exit(0)


