from langchain_text_splitters import RecursiveCharacterTextSplitter

try:
    from .logger import setup_logger
except ImportError:
    from logger import setup_logger

logger = setup_logger(name="splitter")

def splitter(text:str, language:str, chunk_size:int=100, chunk_overlap:int=10):
    logger.debug(f"Splitting text into chunks of size {len(text)} with overlap {chunk_overlap} for language {language}")
    text_splitter = RecursiveCharacterTextSplitter.from_language(language=language, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)

if __name__ == "__main__":
    text = """
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b
    """
    print(splitter(text, "python"))