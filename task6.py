import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['AverageDiscountPercent'], alpha=0.5)
plt.xlabel('Age (Age)')
plt.ylabel('AverageDiscountPercent')
plt.title('Age')
plt.show()

df[df['Age'] > 30]  
filtered_df = df[df['Age'] > 30]
function = filtered_df['AverageDiscountPercent'].mean()
print(f'Average Discount Percent for customers older than 30: {function:.2f}%')
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(filtered_df['AverageDiscountPercent'], vert=False)
plt.xlabel('Average Discount Percent')
plt.title('Boxplot for Average Discount Percent for customers older than 30')
plt.show()
print(f'Boxplot for Average Discount Percent for customers older than 30: {function:.2f}% ')

import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_df, x='AverageDiscountPercent', bins=20, kde=True)
plt.xlabel('Average Discount Percent')
plt.ylabel('Frequency')
plt.title('Distribution of Average Discount Percent for customers older than 30')
plt.show()
