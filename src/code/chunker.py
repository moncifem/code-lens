from constants import get_language_by_extension, filter_directories, contains_ignored_path
from utils import splitter
import os
from utils import setup_logger
logger = setup_logger(name="chunker")

def chunker(path:str, chunk_size:int=100, chunk_overlap:int=10):
    extension = path.split(".")[-1]
    language = get_language_by_extension(extension)
    if language:
        with open(path, "r") as file:
            text = file.read()
            chunks = splitter(text, language, chunk_size, chunk_overlap)
            print(chunks)

def chunk_directory(path:str, chunk_size:int=100, chunk_overlap:int=10):
    for root, dirs, files in os.walk(path):
        dirs[:] = filter_directories(dirs)
        if contains_ignored_path(root):
            continue
        for file in files:
            chunker(os.path.join(root, file), chunk_size, chunk_overlap)
            logger.debug(f"Chunked {file}")

if __name__ == "__main__":
    logger.info("Chunking directory")
    # chunker("src/code/utils/splitter.py")
    chunk_directory("src", chunk_size=1000, chunk_overlap=100)