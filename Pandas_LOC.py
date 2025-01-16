# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:57:16 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")
print(df)

#i location
selected_rows = df.iloc[1:4]
print(selected_rows)


selected_rows1 = df.iloc[:4]
print(selected_rows1)


selected_rows2 = df.iloc[10:]
print(selected_rows2)
