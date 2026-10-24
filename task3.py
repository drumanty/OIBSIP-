import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

total_customer = df['CustomerID'].nunique()

repeat_customers = df[df['ReturnCountLast12Months'] > 1].shape[0]

repeat_rate = repeat_customers / total_customer

churn_rate = 1-repeat_rate

profit_margin = 0.20



clv = ((df['AverageOrderValueINR'].mean())*(df['Purchase_frequency'].mean())*churn_rate)*profit_margin
print(f"Customer Lifetime Value (CLV): ${clv:.2f}")





