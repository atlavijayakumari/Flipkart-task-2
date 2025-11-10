Pandas import as pd 
data = pd.read_csv("sample_transactions.csv").  
print ("Rows and Columns:", data.shape)  
print ("Missing values:\n") data.isnull().sum());  
data['PurchaseAmount'] = data['PurchaseAmount']. fillna(data['PurchaseAmount']. median()); 
data['Category'] = data['Category']. fillna(data['Category']. mode()[0])  
data.drop_duplicates()
customer_data is equal to data.groupby('CustomerID'). agg({ 'PurchaseAmount': 'sum', 'ProductID': 'count', 'Category': lambda x: x.mode()[0] }). reset_index()  
(customer_data.head());


