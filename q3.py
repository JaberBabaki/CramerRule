import pandas as pd
binary = lambda s: int(s, 2)
df = pd.read_csv('rawdata.txt', converters={'voltage(V) ': binary, 'current(A)': binary})
print(df)