import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ---------- Step 1: Load and Prepare the Dataset ----------
# Read the data file
data = pd.read_csv("sample_transactions.csv")

# Clean up and create new features
data.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)
data['PurchaseCount'] = data.groupby('CustomerID')['ProductID'].transform('count')

# Pick the key numeric columns for clustering
features = data[['TotalSpend', 'PurchaseCount']]

# ---------- Step 2: Perform K-Means Clustering ----------
# Group customers into 3 clusters based on spend and purchase behavior
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(features)

# Give each cluster a meaningful name
cluster_names = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}
data['Segment'] = data['Cluster'].map(cluster_names)

# ---------- Step 3: Save the Processed Dataset ----------
data.to_csv("segmented_customers.csv", index=False)
print("✅ Customer segmentation completed successfully!")
print("Saved file: segmented_customers.csv")
print(data.head())

# ---------- Step 4: Create Visualizations ----------

# (1) Scatter plot – relationship between total spend and purchase count
plt.figure(figsize=(7, 5))
plt.scatter(data['TotalSpend'], data['PurchaseCount'], 
            c=data['Cluster'], cmap='viridis', s=60)
plt.title("Customer Segments Based on Spend and Purchases")
plt.xlabel("Total Spend")
plt.ylabel("Purchase Count")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("scatter_segmentation.png")
plt.close()

# (2) Bar chart – number of customers in each segment
plt.figure(figsize=(6, 4))
data['Segment'].value_counts().plot(
    kind='bar', color=['#6A5ACD', '#48D1CC', '#FFA500'])
plt.title("Customer Distribution by Segment")
plt.xlabel("Segment Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("bar_segment_size.png")
plt.close()

# (3) Pie chart – percentage share of each segment
plt.figure(figsize=(5, 5))
data['Segment'].value_counts().plot(
    kind='pie', autopct='%1.1f%%', startangle=90,
    colors=['#FFB6C1', '#87CEFA', '#98FB98'])
plt.title("Customer Segment Proportion")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_segment_distribution.png")
plt.close()

print("📊 All visualizations generated and saved successfully:")
print("   - scatter_segmentation.png")
print("   - bar_segment_size.png")
print("   - pie_segment_distribution.png")
