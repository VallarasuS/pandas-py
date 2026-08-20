## Core Data Structures

```python

import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
```

---

## Indexing & Selection
```python
# Select column
df['Name']

# Select row by label
df.loc[1]

# Select row by position
df.iloc[0]
```

---

## Handling Missing Data
```python
data = pd.Series([1, None, 3, None, 5])

# Detect missing
data.isnull()

# Fill missing
data.fillna(0)

# Drop missing
data.dropna()
```

---

## Input/Output
```python
# Read CSV
df = pd.read_csv('data.csv')

# Write to Excel
df.to_excel('output.xlsx', index=False)
```

---

## Data Wrangling
```python
# Merge
df1 = pd.DataFrame({'id':[1,2], 'val':[10,20]})
df2 = pd.DataFrame({'id':[1,2], 'score':[90,80]})
merged = pd.merge(df1, df2, on='id')

# Concatenate
pd.concat([df1, df2], axis=0)

# Pivot
df.pivot_table(values='Age', index='Name', aggfunc='mean')
```

---

## Visualization
```python
import matplotlib.pyplot as plt

df['Age'].plot(kind='bar')
plt.show()
```

---

## Grouping & Aggregation
```python
# GroupBy
df.groupby('Age').size()

# Aggregate
df.groupby('Age').agg({'Name':'count'})
```

---

## ⏱Time Series
```python
dates = pd.date_range('2024-01-01', periods=5, freq='D')
ts = pd.Series([1,2,3,4,5], index=dates)

# Resample
ts.resample('2D').mean()

# Rolling average
ts.rolling(window=2).mean()
```

---