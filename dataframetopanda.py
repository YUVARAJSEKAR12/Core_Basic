# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:32:49 2024

@author: HP
"""

import pandas as pd
df =pd.read_excel('mark.xlsx')
arrM=df[['Math']].to_numpy().flatten()
print(arrM)
#numpy
arrN=df[['Name']].to_numpy().flatten()
arrM=df[['Math']].to_numpy().flatten()
arrP=df[['Phy']].to_numpy().flatten()
print(arrN)
print(arrM)
print(arrP)
m=arrM+5
print(m)
frame={"Name":arrN, "Math +":m}
dfn=pd.DataFrame(frame)
print(dfn)