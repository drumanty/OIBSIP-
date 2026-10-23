import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\dell\Downloads\retail_sales_5000.xlsx'
df = pd.read_excel(file_path)

raw_age =df['Age']
age_mean = raw_age.mean()
age_median = raw_age.median()
age_counts = raw_age.value_counts()
raw_gender = df['Gender']
gender_counts = raw_gender.value_counts()

print("Age Mean:", age_mean)

print("Age Median:", age_median)

print("\nGender Distribution:")

print(gender_counts)

print("\nAge Distribution:")

print(age_counts)

age_counts.plot(kind='bar', title='Age Distribution')

gender_counts.plot(kind='bar', title='Gender Distribution')

plt.show()

