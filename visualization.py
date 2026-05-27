import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualization():
    data = pd.read_csv('data/expenses_tracker.csv')
    print(data)
    plt.figure(figsize=(9,5))
    plt.subplot(1,2,1)
    plt.title("Category wise expenses")
    sns.barplot(x=data['category'], y=data['amount'])

    plt.subplot(1,2,2)
    plt.title("Count of categories where most expenses are spent")
    sns.countplot(data=data, x=data['category'])
    plt.show()