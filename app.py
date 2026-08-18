import pandas as pd
from pandas import Series, DataFrame

print(pd.__version__)

products = pd.read_csv(r"./data/products.csv")
customers = pd.read_excel(open(r"C:\Users\Valla\Desktop\customers.xlsx", "rb"))
orders = pd.read_csv(r"./data/orders.csv")

print(customers)


