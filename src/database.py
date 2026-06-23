import sqlite3

def create_database():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()


def save_chat(question, answer):
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO chats(question, answer)
        VALUES(?,?)
        """,
        (question, answer)
    )
    conn.commit()
    conn.close()


def get_all_chats():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT question, timestamp
    FROM chats
    ORDER BY id DESC
    """)
    chats = cursor.fetchall()
    conn.close()
    return chats