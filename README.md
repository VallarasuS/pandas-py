# pandas-py

## Installation

```bash
py -m pip install pandas
```

## Quick Start

```python
import pandas as pd

from pandas import Series, DataFrame
```

## Data Structures

### Series

- one dimensional array structure 
containing values and index

```python
s = Series([1, 2, 3, 4])
print(s.values)
print(s.index)
```

### DataFrame

- table like data structure

```python

data = { 
    'col 1': [1, 2, 3], 
    'col 2': ["A", "B", "C"] }

df = DataFrame(data)
```