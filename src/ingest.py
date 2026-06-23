from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.embeddings import get_embeddings
from langchain_chroma import Chroma

def ingest_pdf(pdf_path):
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)
    embeddings = get_embeddings()
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )
    print("PDF processed successfully")