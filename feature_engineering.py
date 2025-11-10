import pandas as pd

# Step 1: Read the dataset
data = pd.read_csv("sample_transactions.csv")
print("Dataset loaded successfully:\n", data.head())

# Step 2: Calculate total spending per customer
total_spent = data.groupby("CustomerID")["PurchaseAmount"].sum().reset_index()

# Step 3: Count how many products each customer purchased
purchase_freq = (
    data.groupby("CustomerID")["ProductID"]
    .count()
    .reset_index()
    .rename(columns={"ProductID": "TotalPurchases"})
)

# Step 4: Find the most frequently purchased category for each customer
top_category = (
    data.groupby("CustomerID")["Category"]
    .agg(lambda x: x.mode()[0])
    .reset_index()
    .rename(columns={"Category": "FavoriteCategory"})
)

# Step 5: Combine all customer insights into one table
customer_summary = (
    total_spent.merge(purchase_freq, on="CustomerID")
    .merge(top_category, on="CustomerID")
)

# Step 6: Display the final summarized data
print("\nCustomer Summary:\n", customer_summary.head())
