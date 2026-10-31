import pandas as pd
file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)




top_customer = (df.groupby('PreferredCategory',dropna=False)['TotalSpendLast12MonthsINR'].sum().reset_index()

.rename(columns={'TotalSpendLast12MonthsINR': 'TotalSpendLast12MonthsINR'})

.sort_values(by='TotalSpendLast12MonthsINR', ascending=False)
)

top_customer = top_customer.head(10)

print("Top 10 Preferred Categories with Highest Total Spend:")
print(top_customer)

