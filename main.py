import time
import os
from expense import Expense
from file_handler import export_csv
from database import create_table

create_table()


print("📈💰📊Welcome to Expense Tracker📈💰📊")
name = input("Enter your name: ").capitalize()

while True:
    obj = Expense(name)
    print("Press\n1. Add expense\n2. View expense\n3. Export CSV\n4. Show analytics\n5. Generate charts\n6. Exit")
    try:
        opt = int(input("Your option: "))
        if opt == 1:
            category = input("Enter category(Food, Travel, Shopping): ").capitalize()
            amount = int(input("Enter how much money spent: "))
            date = input("Enter date(2026-01-01 format): ")
            payment_method = input("Enter payment method(Cash, Card, UPI): ").capitalize()
            note = input("Enter where money spent: ").capitalize()
            Expense.add_expenses(category, amount, date, payment_method, note)
            time.sleep(1)
        elif opt == 2:
            Expense.view_expenses()
            time.sleep(1)
        elif opt == 3:
            file_name = "expenses_tracker.csv"
            ans = os.path.exists(file_name)
            if ans == True:
                print("File already exist")
            else:
                export_csv()


        

        elif opt == 6:
            break 

    except ValueError:
        print("Enter only displayed options")
        time.sleep(1)
    
