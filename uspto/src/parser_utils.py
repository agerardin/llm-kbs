from lxml import etree

# Function to get the element at a given index
def get_element_at_index(file_path, index):
    with open(file_path, "rb") as file:
        for i, (event, element) in enumerate(etree.iterparse(file, tag="{http://www.xml-cml.org/schema}reaction")):
            if i == index:
                return element
    return None

# Function to count the total number of elements
def count_elements(file_path):
    count = 0
    with open(file_path, "rb") as file:
        for event, element in etree.iterparse(file, tag="{http://www.xml-cml.org/schema}reaction"):
            count += 1
    return count

def generate_prompt_examples(exs: list[str,str]):
    ex_prompt = ""
    prompt = """
    example reaction description: {}, 
    example reaction output: {}"""
    for ex in exs:
        ex_prompt += prompt.format(ex[0], ex[1])
    return ex_prompt
