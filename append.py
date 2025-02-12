import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8], 'B': [9, 10]})

# Append df2 to df1
df3 = df1.append(df2, ignore_index=True)

print(df3)

