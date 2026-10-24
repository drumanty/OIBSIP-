import pandas as pd
import numpy as np

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

top_customer = (df.groupby('CustomerID',dropna=False)['Customer_lifetime_value'].sum().reset_index())

max_lifetime_value = top_customer.max()

if max_lifetime_value.empty:
    print("No data available to determine the customer with the highest lifetime value.")

else:
    top_customer = top_customer.sort_values(by='Customer_lifetime_value', ascending=False).head(10)

    print("Top 10 Customers with Highest Lifetime Value:")
    print(top_customer)
    
