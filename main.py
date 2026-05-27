import time
from expense import Expense
from file_handler import export_csv
from database import create_table
from analytics import show_analysis
from animation import animation
from visualization import visualization

create_table()

print('===============================')
print("📈💰📊Welcome to Expense Tracker📈💰📊")
print('===============================')
name = input("Enter your name: ").capitalize()
obj = Expense(name)

while True:
    print('===============================')
    print("Press\n1. Add expense\n2. View expense\n3. Export CSV\n4. Show analytics\n5. Generate charts\n6. Exit")
    print('===============================')
    try:
        opt = int(input("Your option: "))
        if opt == 1:
            category = input("Enter category(Food, Travel, Shopping): ").capitalize()
            amount = int(input("Enter how much money spent: "))
            date = input("Enter date(2026-01-01 format): ")
            payment_method = input("Enter payment method(Cash, Card, UPI): ").capitalize()
            note = input("Enter where money spent: ").capitalize()
            animation("Adding expenses")
            Expense.add_expenses(category, amount, date, payment_method, note)
            print("\nExpenses added!")
        elif opt == 2:
            animation("Loading expenses")
            print('\n')
            Expense.view_expenses()
            time.sleep(1)
        elif opt == 3:
            animation("Exporting CSV")
            print('\n')
            export_csv()
            print("\nExport done")
        elif opt == 4:
            animation("Analyzing data")
            print('\n')
            show_analysis()
        elif opt == 5:
            animation("Generating charts")
            visualization()
            print("Done!")
        elif opt == 6:
            break 

    except ValueError:
        print("Enter only displayed options")
        time.sleep(1)
    
