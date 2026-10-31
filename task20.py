import pandas as pd
import numpy as np


file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

q1 = file_path.quantile(0.25)

q2 = file_path.quantile(0.75)

IQR=q2-q1

lower_bond = q1-(1.5*IQR)
upper_bond = q2-(1.5*IQR)

anomalies = file_path[(file_path<lower_bond) | (file_path>upper_bond)]

print(anomalies)