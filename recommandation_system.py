import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sample_transactions.csv")

# Prepare numeric feature (purchase amount)
X = df[['PurchaseAmount']]

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Segment'] = kmeans.fit_predict(X)

# Map labels to readable names
labels = {0: 'Low Spenders', 1: 'Medium Spenders', 2: 'High Spenders'}
df['SegmentName'] = df['Segment'].map(labels)

# Save and show output
df.to_csv("segmented_customers.csv", index=False)
print("\n✅ Segmentation complete! Saved → segmented_customers.csv")
print(df)

# ---------- Visualization ----------
# Bar chart of spenders
df['SegmentName'].value_counts().plot(kind='bar', color=['skyblue', 'orange', 'lightgreen'])
plt.title('Customer Segment Distribution')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig("customer_segments_bar.png")
plt.show()

# Scatter plot for spending
plt.scatter(df.index, df['PurchaseAmount'], c=df['Segment'], cmap='viridis')
plt.title('Customer Segmentation by Spend')
plt.xlabel('Customer Index')
plt.ylabel('Purchase Amount')
plt.tight_layout()
plt.savefig("customer_segments_scatter.png")
plt.show()

print("\n📊 Charts saved → customer_segments_bar.png & customer_segments_scatter.png")

