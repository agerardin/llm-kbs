"""Process a batch of XML files using a ProcessPoolExecutor."""
import concurrent.futures
from pathlib import Path
from lxml import etree
import time

MAX_WORKERS = 4

def process_element(element):
    # Process the element (e.g., extract data, perform computations)
    # print(f"Processing element: {element.tag}")
    # print(etree.tostring(element).decode())
    return element.tag

def process_file(file_path):
    with open(file_path, "rb") as file:
        for event, record in etree.iterparse(file,tag="{http://www.xml-cml.org/schema}reaction"):
            process_element(record)
    return file_path

def process_dir(dir_path):
    futures = []
    for file_path in dir_path.iterdir():
            with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures.append(executor.submit(process_file, file_path))
                for f in concurrent.futures.as_completed(futures):
                    print(f.result())


if __name__ == "__main__":
    start_time = time.time()
    process_dir(Path("/polus2/gerardinad/projects/llm-kbs/uspto/data/grants/1976"))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
