#head(): 
#head(n) : display starting n row of data frame
#tail(n) : display last n row of data frame

import pandas as pd

df = pd.read_json("sample_Data.json")

print('display 10 rows of first')
print(df.head())

print('display 10 rows of first')
print(df.tail())