import streamlit as st
from src.chatbot import ask_question
st.title("Research Paper Chatbot")
question = st.text_input("Ask a question about the paper:")
if st.button("Ask"):
    if question:
        answer = ask_question(question)
        st.write(answer)