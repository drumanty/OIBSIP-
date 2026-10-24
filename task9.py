import pandas as pd
file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

df['CustomerID'] = df['CustomerID'].astype(str).str.strip()


top_customer = (df.groupby('CustomerID',dropna=False)['AverageOrderValueINR'].sum().reset_index()

.rename(columns={'AverageOrderValueINR': 'TotalOrderValueINR'})

.sort_values(by='TotalOrderValueINR', ascending=False)
)

top_customer = top_customer.head(10)

print("Top 10 Customers with Highest Total Order Value:")
print(top_customer)

