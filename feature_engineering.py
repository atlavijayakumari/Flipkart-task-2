import pandas as pd

data = pd.read_csv("sample_transactions.csv")

print("Dataset loaded successfully:\n", data.head(

total_spent = data.groupby("CustomerID")["PurchaseAmount"].sum().reset_index()

purchase_freq = (

    data.groupby("CustomerID")["ProductID"]

    .count

    .reset_index

    .rename(columns={"ProductID": "TotalPurchases"})

)

    for each customer

top_category = (

    data.groupby("CustomerID")["Category"]

    .agg(lambda x: x.mode()[0])

    .reset_index

    .rename(columns={"Category": "FavoriteCategory)

    total_spent.merge(purchase_freq, on="CustomerID")

    .merge(top_category, on="CustomerID")

)

print("\nCustomer Summary:\n", customer_summary.head())
