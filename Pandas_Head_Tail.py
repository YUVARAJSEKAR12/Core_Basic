# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:01:23 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")
print(df)

h=df.head(2)
t=df.tail(2)
print(h)
print(t)