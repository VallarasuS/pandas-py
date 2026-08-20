import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# # Create
s = Series([1, 2, 3, 4])

# # index
s = Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s["b"])

# # slicing - inclusive of the end value
print(s["a":"c"])

# # operations
print(s * 2)

# # boolean masking
print(s[s > 2])
s[s > 2] = 2

print(s)

a = Series(np.arange(5))
a = a / 0
print(a)

# # null check, boolean  mask
a.isnull()
a[a.isnull()] = 0
print(a)

print(a.fillna(0))
a[a == np.inf] = 1
print(a)

# Data Frame

data = { "names": ["john", "rob", "dave"], "age": [30, 31, 32] }

df = DataFrame(data)
print(df)

df = DataFrame(data, index=["a", "b", "c"])
print(df)

# Series
print(type(df["names"]))  

# sub set of data frame
print(df[["names", "age"]])

# print(df.names)
print(df.age)

df.index = np.arange(3)
print(df)

df.age = df.age + 1
print(df)

df["age"] = 0
print(df)

# drop

# del df["age"]
# print(df)

# df = df.drop("age",  axis = 1)
# print(df)

# indexing numpy
print(df[1:2])

# filtering boolean mask 
print(df["age"] < 31)
print(df[df["age"] < 31])

df1 = pd.DataFrame(np.arange(5))
df2 = pd.DataFrame(np.arange(6))

print(df1)
print(df2)

df3 = df1 + df2
print(df3)

df3 = df1.add(df2, fill_value=0)
print(df3)
