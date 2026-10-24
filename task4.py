import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

recency = df['RecencyDays'].sum()

print(f"Total Recency ${recency:.2f}")

frequency = df['OrdersLast12Months'].sum()
print(f"Total Frequency ${frequency:.2f}")

monetary = df['TotalSpendLast12MonthsINR'].sum()
print(f"Total Monetary ${monetary:.2f}")

rfm = recency + frequency + monetary

print(f"Total RFM is: ${rfm:.2f}")