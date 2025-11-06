import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("sample_transactions.csv")

# Rename and prepare columns
data.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)
data['PurchaseCount'] = data.groupby('CustomerID')['ProductID'].transform('count')

# Select numeric fields for clustering
features = data[['TotalSpend', 'PurchaseCount']]

# Apply K-Means clustering
model = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = model.fit_predict(features)

# Label the groups
labels = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}
data['Segment'] = data['Cluster'].map(labels)

# Save and show results
data.to_csv("segmented_customers.csv", index=False)
print("✅ Segmentation finished → segmented_customers.csv")
print(data.head())

# ---- Visualization ----
plt.figure(figsize=(7,5))
plt.scatter(data['TotalSpend'], data['PurchaseCount'], c=data['Cluster'], cmap='plasma', s=70)
plt.title("Customer Segments based on Spend & Purchases")
plt.xlabel("Total Spend")
plt.ylabel("Purchase Count")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("segmentation_output.png")
plt.show()
print("📊 Graph saved → segmentation_output.png")
