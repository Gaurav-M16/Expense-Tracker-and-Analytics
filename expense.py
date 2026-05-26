from database import get_connection

class Expense:
    
    def __init__(self, name):
        self.name = name
        print(f"Hello, {self.name}")

    @staticmethod
    def add_expenses(category,
                    amount, 
                    date, 
                    payment_method, 
                    note=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses
            (category, amount, date, payment_method, note)
            VALUES (?, ?, ?, ?, ?)
            """, (
                category,
                amount,
                date,
                payment_method,
                note
        ))
        conn.commit()
        conn.close()