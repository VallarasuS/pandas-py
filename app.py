import pandas as pd

from pandas import DataFrame, Series

orders = pd.read_csv(r"./data/orders.csv")
customers = pd.read_csv(r"./data/customers.csv")
products = pd.read_csv(r"./data/products.csv")

df = Series([1,2,3], index=["a", "b", "C"])
df.drop_duplicates(keep=False)
df.dropna()

sales =  pd.merge(
    
    orders, 
    customers, 
    on="customer_id").merge(
        products, 
        on="product_id")

sales["total"] = sales["price"] * sales["quantity"]

print(
    sales.groupby("city")[["total"]]
    .sum()
    .sort_values("total", ascending=False)
    .head(1))

