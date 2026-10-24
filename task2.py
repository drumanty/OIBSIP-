import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

avg_purchase_value = df['AverageOrderValueINR'].mean()
print(f"Average Purchase Value: ${avg_purchase_value:.2f}")