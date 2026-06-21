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
    return response.content