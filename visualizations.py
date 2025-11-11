import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot a
d = pd.read_csv("sample_transactions.c
if 'PurchaseAmount' in d:
    d['TotalSpend'] = d['PurchaseAmou
d['BuyCount'] = d.groupby('CustomerID')['ProductID'].transform('count')
x = d[['TotalSpend','BuyCount']].dropn
km = KMeans(3, random_state=1)
d.loc[x.index,'Grp'] = km.fit_predict(x
d['Name'] = d['Grp'].map({0:'Low',1:'Mid',2:'High'
print("saved out.csv
d['Name'].value_counts().plot.bar(color='pink')
plt.title("Group Sizes")
plt.savefig("bar.jpg")
plt.clos(d['TotalSpend'],d['BuyCount'],c=d['Grp'],cmap='cool')
plt.xlabel("Spend")
plt.ylabel("Count")
plt.title("Groups")
print("bar.jpg and pic.jpg ready")
