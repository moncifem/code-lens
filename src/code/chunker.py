from constants import get_language_by_extension
from utils import splitter
import os

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
        dirs[:] = [d for d in dirs if d not in ['.venv', '__pycache__', '.git', 'node_modules']]
        if any(skip_dir in root for skip_dir in ['.venv', '__pycache__', '.git', 'node_modules']):
            continue
        for file in files:
            chunker(os.path.join(root, file), chunk_size, chunk_overlap)

if __name__ == "__main__":
    # chunker("src/code/utils/splitter.py")
    chunk_directory("src", chunk_size=1000, chunk_overlap=100)