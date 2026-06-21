# test_chatbot.py

from src.chatbot import ask_question

questions = [
    "What is OASIS?",
    "What is Human Robot Interaction?",
    "Summarize the paper in 5 points"
]

for q in questions:

    print("=" * 50)
    print("QUESTION:", q)

    answer = ask_question(q)

    print(answer)