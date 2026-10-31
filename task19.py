import pandas as pd

file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

def create_data_quality_report(df):
    data_type = df.dtypes
    unique_values = df.nunique()

    report_data = pd.DataFrame({
        'Data Type': data_type,
        'Unique Values': unique_values
    })

dq_report = create_data_quality_report(df)
print(dq_report)