import pandas as pd
import numpy as np

df = pd.read_csv("sales_data.csv")


if {'Product', 'Quantity', 'Price'}.issubset(df.columns):
    df["Revenue"] = df["Quantity"] * df["Price"]

    total_revenue = df.groupby("Product")["Revenue"].sum().reset_index()
    print ("Total Revenue per Product:")
    print(total_revenue)
else:
    print ("Error: CSV file must contain 'Product', 'Quantity', and 'Price' columns.")
