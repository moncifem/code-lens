from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def embed_document(document: Document):
    return openai_embeddings.embed_query(document.page_content)

def embed_documents(documents: list[Document]):
    return openai_embeddings.embed_documents([doc.page_content for doc in documents])


if __name__ == "__main__":
    print(embed_document(Document(page_content="Hello, world!")))
