import pandas as pd
import numpy as np

file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

dd= df.drop_duplicates()

print(dd)

co= df.count("columns")


print(co)