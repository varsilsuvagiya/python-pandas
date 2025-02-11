import pandas as pd
dt=pd.read_csv('recipe_dummy_data.csv')
dt.dropna(inplace=True) # drop row of null value
print(dt)
