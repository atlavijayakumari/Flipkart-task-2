import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ---------- Step 1: Load and Prepare Data ----------
data = pd.read_csv("sample_transactions.csv")

# Clean and prepare basic features
data.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)
data['PurchaseCount'] = data.groupby('CustomerID')['ProductID'].transform('count')

# Select numeric data for clustering
features = data[['TotalSpend', 'PurchaseCount']]

# ---------- Step 2: Apply K-Means Clustering ----------
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(features)

# Assign readable segment names
segments = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}
data['Segment'] = data['Cluster'].map(segments)

# ---------- Step 3: Save and Display Dataset ----------
data.to_csv("segmented_customers.csv", index=False)
print("✅ Segmentation Completed → File Saved: segmented_customers.csv")
print(data.head())

# ---------- Step 4: Visualizations ----------

# (1) Scatter Plot: Total Spend vs Purchase Count
plt.figure(figsize=(7, 5))
plt.scatter(data['TotalSpend'], data['PurchaseCount'], c=data['Cluster'], cmap='viridis', s=60)
plt.title("Customer Segments (Spend vs Purchases)")
plt.xlabel("Total Spend")
plt.ylabel("Purchase Count")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("scatter_segmentation.png")
plt.close()

# (2) Bar Chart: Segment Size
plt.figure(figsize=(6, 4))
data['Segment'].value_counts().plot(kind='bar', color=['#6A5ACD', '#48D1CC', '#FFA500'])
plt.title("Number of Customers in Each Segment")
plt.xlabel("Segment Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("bar_segment_size.png")
plt.close()

# (3) Pie Chart: Segment Distribution
plt.figure(figsize=(5, 5))
data['Segment'].value_counts().plot(
    kind='pie', autopct='%1.1f%%', startangle=90, colors=['#FFB6C1', '#87CEFA', '#98FB98']
)
plt.title("Customer Segment Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_segment_distribution.png")
plt.close()

print("📊 All visualizations saved:")
print("   • scatter_segmentation.png")
print("   • bar_segment_size.png")
print("   • pie_segment_distribution.png")
