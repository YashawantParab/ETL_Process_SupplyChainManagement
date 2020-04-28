# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:01:23 2019

@author: yasha
"""

import pandas as pd
import numpy as np

 
df= pd.read_csv("E:\Data Management 2\SCMS_Data2.csv", encoding = "latin_1")
df.head()

df.dtypes

#new data frame with split value columns 
df["product_group"]= df["product_group"].str.split("-", n = 1, expand =True) 

#replace + to /  and remove unwanted /
df['dosage'] = df['dosage'].str.rstrip('+/')

df['dosage'] = df['dosage'].str.replace(r'+','/')

#Remove $ from Cost
df['freight_cost'] = df['freight_cost'].str.replace(r'$','')


#drop null values
#df.dropna(inplace = True)

#saving as csv
#df.to_csv(r'E:\Data Management 2\SCMS_Data3.csv', index=False) 


#prediction
df.info()

df.freight_cost.describe()

#making string to integer 0
df['freight_cost'] = df['freight_cost'].str.replace(r'Freight Included in Commodity Cost','0')


df['freight_cost'] = df['freight_cost'].str.replace(r'nan','0')


df.fillna(0)
#fill nan value to 0
df['freight_cost'] = df['freight_cost'].fillna(0)

df['freight_cost'].count()


"""

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
test_new = test.drop('freight_cost', axis=1)
y_test = np.log1p(test["freight_cost"])
train = train[train.price != 0].reset_index(drop=True)


nrow_train = train.shape[0]
y = np.log1p(train["freight_cost"])
merge: pd.DataFrame = pd.concat([train, test_new])
"""


import petl as etl

table1 = [['foo', 'bar', 'baz'],
           ['orange', 12, 'oranges are nice fruit'],
           ['mango', 42, 'I like them'],
           ['banana', 74, 'lovely too'],
           ['cucumber', 41, 'better than mango']]

# Regular expression search to find any field having g letter in it
table2 = etl.search(table1, '.g')
print(table2)
















