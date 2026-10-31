import pandas as pd
import numpy as np

file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

df= pd.DataFrame({
    "A": [1,np.nan,3,np.nan],
    "B": [np.nan,10,np.nan,40]
    
})

df_filled = df.ffill()

print(df_filled)