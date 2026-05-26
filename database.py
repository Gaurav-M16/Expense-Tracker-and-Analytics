import sqlite3

conn = sqlite3.connect("data/expenses.db")

cursor = conn.cursor()

conn.commit()
conn.close()