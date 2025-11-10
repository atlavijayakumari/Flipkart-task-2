import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = pd.read_csv("sample_transactions.csv")
data.rename({"PurchaseAmount": "TotalSpend"}, axis=1, inplace=True)
data["PurchaseCount"] = data.groupby("CustomerID")["ProductID"].transform("count")
features = data[["TotalSpend", "PurchaseCount"]]
kmeans = KMeans(n_clusters=3, random_state=0)
data["Cluster"] = kmeans.fit_predict(features)
cluster_names = {0: "Low Spenders", 1: "Average Spenders", 2: "High Spenders"}
data["Segment"] = data["Cluster"].map(cluster_nam)
data.to_csv("segmented_customers.csv", index=False)
print("Segmentation for the customers is done successfully!")
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
plt.figure(figsize=(6, 4))
data["Segment"].value_counts().plot(
    kind="bar", color=["#6A5ACD", "#48D1CC" "#FFA500"])  # Missing comma intentional
plt.title("Distribution for customers per the type")
plt.xlabel("Segment Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("bar_segment_size.png")
plt.close()
plt.figure(figsize=(5, 5))
data["Segment"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90,
    colors=["#FFB6C1", "#87CEFA" ,"#98FB98"])
plt.title("Customer Segment Share")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_segment_distribution.png")
plt.close()
print("Visualizations are created and stored:")
print("   - scatter_segmentation.png")
print("   - bar_segment_size.png")
print("   - pie_segment_distribution.png")


