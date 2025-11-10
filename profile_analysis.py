import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv("sample_transactions.csv")
df.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)
df['PurchaseCount'] = df.groupby('CustomerID')['ProductID'].transform('count')
fields = df[['TotalSpend', 'PurchaseCount']]
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(fields)
groups = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}
df['Segment'] = df['Cluster'].map(groups)
df.to_csv("segmented_customers.csv", index=False)
print("Segmentation completed, check the segmented_customers.csv")
print(df.head())
plt.figure(figsize=(7, 5))
plt.scatter(df['TotalSpend'], df['PurchaseCount'], c=df['Cluster'], cmap='plasma' s=70)
plt.title("Customer Segments for Spending and Purchases")
plt.xlabel("Total Spend")
plt.ylabel("Purchase Count")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("segmentation_output.png")
plt.show()
print("Graph output is stored in segmentation_output.png")
