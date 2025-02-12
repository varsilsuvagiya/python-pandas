import pandas as pd

# Create a sample DataFrame
data = {'foo': ['one','one','one','two','two','two'],
        'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
        'baz': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

# Use pivot
pivoted = df.pivot(index='foo', columns='bar', values='baz')

print(pivoted)
