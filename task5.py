import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

file_path = r'C:\Users\dell\Downloads\ecommerce_customer_segmentation_5000.xlsx'
df = pd.read_excel(file_path)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['CustomerTenureDays', 'WebsiteVisitsLast12Months', 'EmailOpenRatePercent']])

inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(df_scaled)
    inertia.append(model.inertia_)

plt.plot(range(1, 11), inertia)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

Kmeans= KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = Kmeans.fit_predict(df_scaled)

score = silhouette_score(df_scaled, df['Cluster'])
print(f'Silhouette Score: {score:.2f}')

summary = df.groupby('Cluster').agg({
    'CustomerTenureDays': ['mean', 'std'],
    'WebsiteVisitsLast12Months': ['mean', 'std'],
    'EmailOpenRatePercent': ['mean', 'std']
})

print(summary)

plt.figure(figsize=(10, 6))
plt.scatter(df['CustomerTenureDays'], df['WebsiteVisitsLast12Months'], c=df['Cluster'], cmap='viridis', alpha=0.6)
plt.xlabel('Customer Tenure (Days)')
plt.ylabel('Website Visits (Last 12 Months)')
plt.title('Customer Segments')
plt.show()

for cluster in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster]
    plt.figure(figsize=(10, 6))
    plt.hist(cluster_data['EmailOpenRatePercent'], bins=20, alpha=0.7)
    plt.xlabel('Email Open Rate (%)')
    plt.ylabel('Frequency')
    plt.title(f'Email Open Rate Distribution for Cluster {cluster}')
    plt.show()

