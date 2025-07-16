from code.utils import setup_logger
from vector_store.chroma_db import get_vector_store
from embedding import embed_document, embed_documents


logger = setup_logger(name="main")

def main():
    vector_store = get_vector_store("code_base", embed_document)
    print(vector_store.get())


if __name__ == "__main__":
    logger.info("Starting CodeLens")
    main()
