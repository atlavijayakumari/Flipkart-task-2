import pandas as pd

# Load dataset
df = pd.read_csv("sample_transactions.csv")
print("Data loaded successfully\n", df.head())

# Total amount spent by each customer
total_spend = df.groupby("CustomerID")["PurchaseAmount"].sum().reset_index()

# Number of purchases made by each customer
purchase_count = df.groupby("CustomerID")["ProductID"].count().reset_index()
purchase_count.rename(columns={"ProductID": "TotalPurchases"}, inplace=True)

# Most common category bought by each customer
fav_category = df.groupby("CustomerID")["Category"].agg(lambda x: x.mode()[0]).reset_index()
fav_category.rename(columns={"Category": "FavCategory"}, inplace=True)

# Merge all features together
customer_data = total_spend.merge(purchase_count, on="CustomerID").merge(fav_category, on="CustomerID")

# Show the final data
print("\nFinal Customer Features:\n", customer_data.head())