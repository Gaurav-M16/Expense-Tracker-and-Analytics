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
                    note):
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
    
    @staticmethod
    def view_expenses():
        conn = get_connection()
        cursor = conn.cursor()
        statement = """SELECT * FROM expenses"""
        cursor.execute(statement)
        output_all = cursor.fetchall()
        for row in output_all:
            print(row)

        conn.commit()
        conn.close()