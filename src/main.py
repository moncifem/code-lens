from code.utils import setup_logger
from vector_store.chroma_db import get_vector_store
from embedding import embed_document, embed_documents
from code.utils.downloader import download_repo
from code.chunker import chunk_directory
import os

logger = setup_logger(name="main")

def main():
    vector_store = get_vector_store("code_base", embed_document)
    repo_url = 'https://github.com/moncifem/code-lens.git'
    if not os.path.exists('./CodeLens'):
        download_repo(repo_url, './CodeLens')
    chunks = chunk_directory('CodeLens')
    print(chunks)


if __name__ == "__main__":
    logger.info("Starting CodeLens")
    main()
