import pandas as pd
file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)




top_customer = (df.groupby('CustomerID',dropna=False)['AverageDiscountPercent'].sum().reset_index()

.rename(columns={'AverageDiscountPercent': 'TotalAverageDiscountPercent'})

.sort_values(by='TotalAverageDiscountPercent', ascending=False)
)

top_customer = top_customer.head(10)

print("Top 10 Customers with Highest Total Average Discount Percent:")
print(top_customer)

