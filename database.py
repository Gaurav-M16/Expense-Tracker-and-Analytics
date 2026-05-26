import sqlite3


def get_connection():
    conn = sqlite3.connect("data/expenses.db")
    return conn


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        date TEXT,
        payment_method TEXT,
        note TEXT
    )
    """)

    conn.commit()
    conn.close()