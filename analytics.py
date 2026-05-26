import pandas as pd

def show_analysis():
    df = pd.read_csv("data/expenses_tracker.csv")
    total_spending = df['amount'].sum()
    avg_spending = df['amount'].mean()
    high_expense = df['amount'].max()
    grp = df.groupby('category')['amount'].sum()
    print(f"\nTotal spending done is: {total_spending}")
    print(f"Average spending done is: {avg_spending}")
    print(f"Highest spending done is: {high_expense}")
    print(f"Data grouped by category: \n{grp}\n\n")