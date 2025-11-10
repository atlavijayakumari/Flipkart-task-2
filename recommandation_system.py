import pandas from sklearn.cluster import as pd.  Import matplotlib.pyplot as plt in KMeans  
# Import data 
df = pd.read_csv ("sample_transactions.csv")  
# Get the purchase amount numerical feature ready.
X = df[['PurchaseAmount']]  
# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  df['Segment'] = kmeans.fit_predict(X)  
# Assign readable names to labels  
labels = {0: 'Low Spenders', 1: 'Medium Spenders', 2: 'High Spenders'}  df['SegmentName'] = df['Segment']. map (labels)  
# Save and display the result 
(df.to_csv ("segmented_customers.csv", index=False).  Segmentation is finished!  Segmented_customers.csv is saved.  print (df)  
# ----------  Visualisation  ---------- 
#Spenders' bar chart  df['SegmentName']. value_counts(). plot(kind='bar', color='skyblue', 'orange', 'lightgreen'])  
plt.title ('Customer Segment Distribution')  
plt.xlabel ('Segment')  
plt.ylabel('Number of Customers') 
plt.tight_layout() 
plt.savefig ("customer_segments_bar.png") 
plt.show()  
# Spending scatter plot  plt.scatter(df.index, df['PurchaseAmount'], c=df['Segment'], cmap='viridis')  plt.title ('Customer Segmentation by Spend')  plt.xlabel ('Customer Index')  plt.ylabel ('Purchase Amount')  plt.tight_layout()  plt.savefig ("customer_segments_scatter.png")  plt.show()  
print( "\n📊 Charts saved → customer_segments_bar.png & customer_segments_scatter.png" )
