import pandas as pd

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

cus_id = df['CustomerID']
quality = df['Customer_Type']


cus_id=cus_id.head(5)
quality=quality.head(5)

print(cus_id)
print(quality)