import pandas as pd


file_path = r"C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000 (1).xlsx"
df = pd.read_excel(file_path)

def create_data_quality_report(df):
    data_type = df.dtypes
    total_rows = len(df)
    missing_value = df.isnull().sum()
    missing_percentage = (missing_value/total_rows)*100
    unique_values = df.nunique()



    report = pd.DataFrame({
        'Data Type': data_type,
        'Total Rows': total_rows,
        'Missing Value': missing_value,
        'Missing Percentage': missing_percentage,
        'Unique Values': unique_values
    })


    numeric_cols = df.select_dtypes(include=['number']).columns
    report['Min'] = df[numeric_cols].min()
    report['Max'] = df[numeric_cols].max()
    report['Mean'] = df[numeric_cols].mean().round(2)
    
    return report

dq_report = create_data_quality_report(df)

print(dq_report)