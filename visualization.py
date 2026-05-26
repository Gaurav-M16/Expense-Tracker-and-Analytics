import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/expenses_tracker.csv')
print(data)
plt.plot(data['amount'])
plt.show()