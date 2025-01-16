# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:26:42 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")
#df = pd.read_csv("mark.csv")
print(df)

information=df.info()
print(information)

size=df.size
print(size)

shape=df.shape
print(shape)

col = df[["Name","Phy"]]
print(col)

#col.to_excel()
col.to_excel('output5.xlsx', index=False)