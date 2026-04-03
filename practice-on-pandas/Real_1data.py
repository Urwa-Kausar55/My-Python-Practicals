import pandas as pd
df= pd.read_csv("ecommerce_sales_data.csv")
print(df.head())#it shows 1st 5 rows 
print(df.shape)# it gives number of rows an column
print("total earnings",df["Total Sales"].sum())# it summ out the column of Total Sales
print("most expensive item",df["Price"].sum())# it gives maximum price of an item
print(df.columns)# it display all column 
print(df.info)# it checks the column is empty or not 
print(df.describe)