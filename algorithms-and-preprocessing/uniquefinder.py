import pandas as pd

data = pd.read_csv('unique.csv', header=None)
uniqueArray = data[0].unique()

print(len(uniqueArray))
