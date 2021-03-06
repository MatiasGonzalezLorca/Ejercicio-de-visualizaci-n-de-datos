# -*- coding: utf-8 -*-
"""Datos 1.5Proyecto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12bbjC8ciqk-JMHNmyufSuzhsdnBMTEG0
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

filename = '/content/drive/MyDrive/Curso coding dojo/dataset/sales_predictions.csv'
df = pd.read_csv(filename)
df

df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)

#median=df['Outlet_Size'].mode()
df['Item_Weight'].fillna(df['Item_Weight'].replace('','Medium'),inplace=True)
df

#df['Outlet_Identifier'].fillna(df['Outlet_Identifier'].replace({'': 'OUT049'}, regex=True))
df['Outlet_Size'].fillna( method ='ffill', inplace = True)
df

df['Item_Visibility'].replace(0,df['Item_Visibility'].mean(),inplace=True)

df['Item_Visibility'].mean()

df.info()

df['Item_Outlet_Sales'].hist()

price_filter = df.loc[:, 'Item_Outlet_Sales'] >0
df.loc[price_filter, 'Outlet_Location_Type'].hist(bins = 30,
                                   edgecolor='black')

val = pd.DataFrame(df.groupby(['Item_MRP', 'Outlet_Location_Type', 'Outlet_Type'])['Item_Outlet_Sales'].mean())
val

val2 = val.reset_index().groupby(['Item_MRP', 'Outlet_Location_Type'])['Item_Outlet_Sales'].apply(list)
val2

val3 = val2.reset_index()
val3

nanFil = val3.loc[:, 'Item_Outlet_Sales'].apply(lambda x: np.logical_not(np.isnan(x).any()))
# filtrar USA
usFil = val3['Outlet_Location_Type'] == 'Tier 2'

nanFil & usFil

val4 = val3.loc[nanFil & usFil , :]
val4

val4['Item_Outlet_Sales'].values

val4['Item_MRP'].values[0]





plt.style.use('seaborn')
indexList = []
for index, heights in enumerate(val3['Item_Outlet_Sales'].values):
  plt.boxplot(val4['Item_Outlet_Sales'].values[index],
              positions = [index],
              widths = .6,
              medianprops = dict(linestyle='-', linewidth=2, color='green'),
              showmeans = True,
              meanprops =dict(marker='X', markeredgecolor='black',
              markerfacecolor='firebrick'))
  indexList.append(index)
plt.xticks(indexList,val4['Outlet_Location_Type'].values, fontsize = 16, rotation = 45)
plt.yticks(fontsize = 16)
plt.title('US Olympic Heights Over Time', fontsize = 18)

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import mean_squared_error

X = df[[ 'Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]
y= df['Item_Outlet_Sales']
X.shape

scaler = StandardScaler()
scaler.fit(X)
X=scaler.transform(X)

knn_reg=KNeighborsRegressor(n_neighbors=2)
knn_reg.fit(X,y)

predic=knn_reg.predict(X)

knn_reg.score(X,y)

np.sqrt(mean_squared_error(y,predic))

scaler=StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

y.value_counts()

