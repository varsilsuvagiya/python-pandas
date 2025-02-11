import pandas as pd

# Load data
df = pd.read_csv('recipe_dummy_data.csv')

# Fill NaN values with a specified value (e.g., 0)
df.fillna('varrr', inplace=True)

print(df)

