# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:10:53 2019

@author: yashawant Parab
"""

import pandas as pd
import numpy as np

df= pd.read_csv("E:\Data Management 2\Supply_Chain_Shipment_Pricing_Data.csv")
df.head()

maindf = df[['id','country','managed by','vendor inco term',
            'shipment mode','product group','vendor','dosage form',
            'line item quantity','weight (kilograms)',
            'freight cost (usd)']]

#Delete Data with NaN and Null
maindf.dropna(inplace = True)
print(maindf)


GCountry = df.groupby('country')
GCountry.first()

GCountry.get_group('Benin')
print(GCountry)
