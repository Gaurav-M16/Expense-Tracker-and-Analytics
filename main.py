import time

while True:
    print("📈💰📊Welcome to Expense Tracker📈💰📊")
    print("Press\n1. Add expense\n2. View expense\n3. Export CSV\n4. Show analytics\n5. Generate charts\n6. Exit")
    try:
        opt = int(input("Your option: "))
        if opt == 6:
            break
    except ValueError:
        print("Enter only displayed options")
        time.sleep(1)
    
