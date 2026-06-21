from langchain_chroma import Chroma

def get_retriever(embeddings):
    vector_store = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 8}
    )
    return retriever