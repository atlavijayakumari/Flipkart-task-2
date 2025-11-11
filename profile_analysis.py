import pandas as pd

from sklearn.cluste

import matplotlib.pyplot as plt

df = pd.read_csv("sample_transactions.csv")

df.rename(columns={'PurchaseAmount': 'TotalSpend'}

fields = df[['TotalSpend', 'PurchaseCount']]

kmeans = KMeans(n_clusters=3, random_state=0)

df['Cluster'] = kmeans.fit_predict(fields)

groups = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}


df.to_csv("segmented_customers.csv", index=False)

print(df.head())

plt.figure(figsize=(7, 5))

c=df['Cluster'], cmap='plasma' s=70)

plt.title("Customer Segments for Spending and Purchases")

plt.xlabel("Total Spend")

plt.tight_layout()

plt.saveegmentation_output.png")


print("Graph output is stored in segmentation_output
