from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    load_dotenv()
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )
    return llm