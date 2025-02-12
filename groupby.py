import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'John', 'Anna', 'John', 'Anna'],
        'Age': [28, 24, 28, 24, 28, 24],
        'Score': [90, 80, 70, 60, 50, 40]}
df = pd.DataFrame(data)

# Group by a column and calculate the mean of a column
grouped = df.groupby('Name')
mean_score = grouped['Score'].mean()

print(mean_score)
