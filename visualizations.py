import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ---------- Step 1: Load Dataset ----------
df = pd.read_csv("sample_transactions.csv")

# Fix column names if needed
if 'TotalSpend' not in df.columns and 'PurchaseAmount' in df.columns:
    df.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)

# If PurchaseCount missing, calculate it
if 'PurchaseCount' not in df.columns and 'CustomerID' in df.columns:
    df['PurchaseCount'] = df.groupby('CustomerID')['ProductID'].transform('count')

# ---------- Step 2: Apply K-Means ----------
X = df[['TotalSpend', 'PurchaseCount']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Segment'] = kmeans.fit_predict(X)

# Add readable segment names
names = {0: 'Low Spenders', 1: 'Average Spenders', 2: 'High Spenders'}
df['SegmentName'] = df['Segment'].map(names)

# ---------- Step 3: Save Segmented Data ----------
df.to_csv("segmented_customers.csv", index=False)
print("\n✅ Segmentation completed → segmented_customers.csv")

# ---------- Step 4: Visualizations ----------
# Bar chart – number of customers per segment
df['SegmentName'].value_counts().plot(kind='bar', color=['skyblue', 'orange', 'lightgreen'])
plt.title('Customer Segments Count')
plt.xlabel('Segment Type')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig("segmented_bar_chart.png")
plt.close()

# Scatter plot – clustering visualization
plt.scatter(df['TotalSpend'], df['PurchaseCount'], c=df['Segment'], cmap='viridis', s=60)
plt.title('Customer Segmentation Visualization')
plt.xlabel('Total Spend')
plt.ylabel('Purchase Count')
plt.tight_layout()
plt.savefig("segmented_scatter_plot.png")
plt.close()

print("\n📊 Visualizations automatically saved:")
print("   • segmented_bar_chart.png")
print("   • segmented_scatter_plot.png")
