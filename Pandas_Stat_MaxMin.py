# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:12:58 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")
#print(df)

df1 = df[["Bio","Phy","Math","Tamil","Eng"]]
ma=df1.max()
print(ma)

df1 = df[["Bio","Phy","Math","Tamil","Eng"]]
min=df1.min()
print(min)

