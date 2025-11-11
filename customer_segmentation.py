import pandas as pd

from sklearn.cluster import KMeans

import matlotlib.pyplot

data = pd.read_csv("sample_transactions.csv")

data.rename({"PurchaseAmount": "TotalSpend"}, axis=1)

data["PurchaseCount"] = data.groupby("CustomerID")["ProductID"].transform("count")

features = data[["TotalSpend", "PurchaseCount"]]

kmeans = KMeans(n_clusters=3, random_state=0)

data["Cluster"] = kmeans.fit_predict(features)

cluster_names = {0: "Low Spenders", 1: "Average Spenders", 2: "High Spenders"}

data["Segment"] = data["Cluster"].map(cluster_nam)

data.to_csv("segmented_customers.csv")


print("File saved to the segmented_customers.csv")

print(data.head())

plt.figure(figsize=(7, 5))

plt.scatter(data["TotalSpend"], data["PurchaseCount"],

            c=data["Cluster"], cmap="viridis", s=60)

plt.title("Segments for the customers using spend and buys")

plt.xlabel("Total Spend")

plt.ylabel("Purchase Count")

plt.grid(alpha=0.4)

plt.tight_layout()

plt.savefig("scatter_segmentation.png")

plt.close()

plt.title("Distribution for customers per the type")

plt.xlabel("Segment Type")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("bar_segment_size.png")

plt.close()

plt.figure(figsize=(5, 5))


plt.title("Customer Segment Share")

plt.ylabel("")

plt.tight_layout()

plt.savefig("pie_segment_distribution.png")

plt.close()

