import sqlite3

conn = sqlite3.connect("data/expenses.db")

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               category TEXT,
               amount REAL,
               data TEXT,
               payment_method TEXT,
               note TEXT)

""")

conn.commit()
conn.close()