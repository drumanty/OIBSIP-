import pandas as pd
import numpy as np

file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)
print(df)

def double(num):
    return num * 2

numbers =[1,2,3]

doubled_numbers = list(map(double, numbers))

print(doubled_numbers)


def create_data (ds):
    file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
    ds = pd.read_excel(file_path)
    for i in range ds:

        print(ds)
        sa = ds('customerID')
        if ds in sa:
            print(sa)

        else:
            print("File is not exit")

    