import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

plt.bar(df['Age'], df['PreferredCategory'])
plt.xlabel('Age')
plt.ylabel('Preferred Category')
plt.title('Age vs. Preferred Category')
plt.show()