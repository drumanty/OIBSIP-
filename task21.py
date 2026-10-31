import pandas as pd
import numpy as np

file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

im = df['AverageOrderValueINR'].sum()

pu = df['TotalSpendLast12MonthsINR'].sum()

temp = (im + pu)

temp1= 1-(temp/100)

imputation= (temp1*100)/225

if imputation>1:
    print("Pure Imputation:",(imputation))

else:
    print("Impure Imputation:",(imputation))


