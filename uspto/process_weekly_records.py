from concurrent.futures import ThreadPoolExecutor

import lxml.etree as ET


def process_element(element):
    # Process the element (e.g., extract data, perform computations)
    print(f"Processing element: {element.tag}")


def parse_large_xml(file_path):
    context = ET.iterparse(file_path, events=("end",), tag="reactant")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for event, elem in context:
            futures.append(executor.submit(process_element, elem))
            # Clear the element from memory to save space
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        # Wait for all futures to complete
        for future in futures:
            future.result()


if __name__ == "__main__":
    parse_large_xml("/polus2/gerardinad/data/uspto/pftaps19760106_wk01.xml")
