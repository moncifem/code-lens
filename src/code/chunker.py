from constants import get_language_by_extension
from utils import splitter

def chunker(path:str):
    extension = path.split(".")[-1]
    language = get_language_by_extension(extension)
    if language:
        with open(path, "r") as file:
            text = file.read()
            chunks = splitter(text, language)
            print(chunks)

if __name__ == "__main__":
    chunker("src/code/utils/splitter.py")