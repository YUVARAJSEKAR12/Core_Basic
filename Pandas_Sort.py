# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:03:43 2024

@author: HP
"""
import pandas as pd

df = pd.read_excel("mark.xlsx")
#print(df)

sort=df.sort_values(by=["Math"])
print(sort)


dsort=df.sort_values(by='Math', ascending=False)
print(dsort)
