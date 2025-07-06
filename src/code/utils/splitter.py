from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitter(text:str):
    text_splitter = RecursiveCharacterTextSplitter.from_language(language="python", chunk_size=100, chunk_overlap=10)
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
    print(splitter(text))