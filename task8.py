import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


file_path = r'C:\Users\dell\Downloads\retail_sales_5000.xlsx'
df = pd.read_excel(file_path)

corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(16, 14))

# 4. Generate the heatmap
sns.heatmap(
    corr_matrix,
    annot=True,  # Shows the numerical correlation value in each cell
    cmap="coolwarm",  # Good diverging palette (blue = negative, red = positive)
    fmt=".2f",  # Rounds values to 2 decimal places
    vmin=-1,
    vmax=1,  # Sets limits to match Pearson's correlation range
    linewidths=1.5,  # Adds a visible grid separating the cells
)

# 5. Final graph display tweaks

plt.tight_layout()
plt.show()
