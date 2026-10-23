import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\retail_sales_5000.xlsx'
df = pd.read_excel(file_path)



# Convert dates, supporting text and native Excel dates
raw_dates = df['Date']

if pd.api.types.is_numeric_dtype(raw_dates):
    # Excel date serial numbers
    df['Date'] = pd.to_datetime(
        raw_dates, unit='D', origin='1899-12-30', errors='coerce'
    )
else:
    df['Date'] = pd.to_datetime(
        raw_dates.astype(str).str.strip(),
        format='mixed',
        dayfirst=True,
        errors='coerce'
    )

# Convert sales amounts to numeric
df['Total Amount'] = pd.to_numeric(
    df['Total Amount'].astype(str).str.replace(',', '', regex=False),
    errors='coerce'
)

print("\nValid dates:", df['Date'].notna().sum())
print("Valid sales:", df['Total Amount'].notna().sum())
print("Date range:", df['Date'].min(), "to", df['Date'].max())

# Remove invalid dates and sales
df = df.dropna(subset=['Date', 'Total Amount'])

if df.empty:
    print("ERROR: No valid date and sales rows found.")
else:
    # Group sales by month, without restricting to 2023
    monthly_sales = (
        df.set_index('Date')['Total Amount']
        .resample('MS')
        .sum()
    )

    print("\nMonthly sales:")
    print(monthly_sales)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker='o',
        color='crimson',
        linewidth=2
    )

    plt.title('Monthly Retail Sales Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Sales Revenue')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
