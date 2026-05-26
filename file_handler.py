import pandas as pd
from database import get_connection

conn = get_connection()

def export_csv():
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_csv("expenses_tracker.csv", index=False)
    conn.commit()
    conn.close()

