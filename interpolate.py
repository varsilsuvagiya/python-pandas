import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('recipe_dummy_data.csv')

# Interpolate missing values
df['Description'].interpolate(method='pad', inplace=True)

print(df)
