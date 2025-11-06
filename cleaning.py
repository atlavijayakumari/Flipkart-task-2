import pandas as pd

# Step 1: Load the dataset
data = pd.read_csv("sample_transactions.csv")

# Step 2: View basic info
print("Rows and Columns:", data.shape)
print("Missing values:\n", data.isnull().sum())

# Step 3: Fill missing values
data['PurchaseAmount'] = data['PurchaseAmount'].fillna(data['PurchaseAmount'].median())
data['Category'] = data['Category'].fillna(data['Category'].mode()[0])

# Step 4: Remove duplicate rows
data = data.drop_duplicates()

# Step 5: Create new customer summary table
customer_data = data.groupby('CustomerID').agg({
    'PurchaseAmount': 'sum',
    'ProductID': 'count',
    'Category': lambda x: x.mode()[0]
}).reset_index()

# Step 6: Display result
print(customer_data.head())



