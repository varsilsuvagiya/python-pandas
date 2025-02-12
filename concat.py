import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=[0, 1, 2])

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                     'B': ['B3', 'B4', 'B5']},
                    index=[3, 4, 5])

df3 = pd.DataFrame({'A': ['A6', 'A7', 'A8'],
                     'B': ['B6', 'B7', 'B8']},
                    index=[6, 7, 8])

df4 = pd.DataFrame({'A': ['A9', 'A10', 'A11'],
                     'B': ['B9', 'B10', 'B11']},
                    index=[9, 10, 11])

df5 = pd.concat([df1, df2, df3, df4])
print(df5)
