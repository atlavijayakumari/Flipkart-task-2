import pandas as pd
txns = pd.read_csv("sample_transactions.cs
print(f"Dataset size → {txns.shape[0]} rows, {txns.shape[1]} columns")
print("\nNull count per column:")
print(txns.isna().su
median_amount = txns['PurchaseAmount'].median()
txns['PurchaseAmount'] = txns[
most_common_cat = txns['Category'].mode()[0]
txns['Category'] = txns['Category'].fillna(most_common_cat)
txns = txns.drop_duplicates().reset_index(drop=T
cust_summary = (
    txns.groupby('CustomerID', as_index=False)
        .agg(
            total_spent=('PurchaseAmount', 'sum'),
            purchase_count=('ProductID', 'count'),
            top_category=('Category', lambda s: s.mode().iloc[0])
        )
print("\nFirst 5 customer records:")
print(cust_summary.head())
