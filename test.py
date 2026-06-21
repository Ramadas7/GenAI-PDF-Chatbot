from src.pdf_loader import load_pdf
from src.text_splitter import split_documents

docs = load_pdf("C:\\Users\\kotip\\Desktop\\GenAI_Chatbot\\data\\sample.pdf")
chunks = split_documents(docs)
print("Pages:", len(docs))
print("Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])