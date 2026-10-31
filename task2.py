import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\dell\Downloads\retail_sales_5000.xlsx'
df = pd.read_excel(file_path)

print('Shape:', df.shape)
print('Number of rows:', df.shape[0])
print('Number of columns:', df.shape[1])


plot = df.plot(x='Date', y='Total Amount', kind='line', title='Retail Sales Over Time')
print('Plot created successfully.')


plt.show()