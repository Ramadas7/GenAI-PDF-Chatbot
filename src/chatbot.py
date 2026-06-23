from src.embeddings import get_embeddings
from src.retriever import get_retriever
from src.llm import get_llm

embeddings = get_embeddings()
retriever = get_retriever(embeddings)
llm = get_llm()

def ask_question(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    prompt = f"""
    Answer the question using ONLY the provided context.
    Context:
    {context}
    Question:
    {question}
    Answer:
    """
    response = llm.invoke(prompt)
    sources = []
    for doc in docs:
        page = doc.metadata.get("page", "Unknown")
        if page != "Unknown":
            sources.append(f"Page {page + 1}")
        else:
            sources.append("Unknown Page")
    sources = list(set(sources))
    return {
        "answer": response.content,
        "sources": sources
    }