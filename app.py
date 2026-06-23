from flask import Flask, render_template, request, redirect
from src.chatbot import ask_question
import os
from src.ingest import ingest_pdf
from src.database import create_database, save_chat, get_all_chats

app = Flask(__name__)
create_database()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/", methods=["GET", "POST"])
def upload_page():
    if request.method == "POST":
        file = request.files["pdf"]
        if file.filename == "":
            return "No file selected"
        pdf_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )
        file.save(pdf_path)
        ingest_pdf(pdf_path)
        return redirect("/chat")
    return render_template("uploads.html")
@app.route("/chat", methods=["GET", "POST"])
def chat_page():
    answer = ""
    sources = []
    if request.method == "POST":
        question = request.form["question"]
        result = ask_question(question)
        answer = result["answer"]
        save_chat(question, answer)
        sources = result["sources"]
        chat_history = get_all_chats()
    return render_template(
        "chat.html",
        answer=answer,
        sources=sources,
        chat_history=chat_history
    )
if __name__ == "__main__":
    app.run(debug=True)