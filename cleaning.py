Pandas import as pd 
# First, load the dataset using 
data = pd.read_csv("sample_transactions.csv"). 
 # Step 2: View basic information  
print ("Rows and Columns:", data.shape)  
print ("Missing values:\n") data.isnull().sum());  
# Step 3: Complete the following fields: data['PurchaseAmount'] = data['PurchaseAmount']. fillna(data['PurchaseAmount']. median()); 
data['Category'] = data['Category']. fillna(data['Category']. mode()[0])  
# Step 4: Use 
data.drop_duplicates() 
to eliminate duplicate rows.  
# Create a new customer summary table in step five. 
customer_data is equal to data.groupby('CustomerID'). agg({ 'PurchaseAmount': 'sum', 'ProductID': 'count', 'Category': lambda x: x.mode()[0] }). reset_index()  
# Step 6: Print the outcome 
(customer_data.head());
