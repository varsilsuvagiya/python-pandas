import pandas as pd
a=pd.Series( [1,2,3,4,5] )
# a=pd.Series( [1,2,3,4,5],dtype="float" )
# a=pd.Series( [1,2,3,4,5] ,index=["a","b","c","d","e"])
print(a)
print(type(a))