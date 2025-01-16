# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:10:09 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")
#print(df)

replace=df.replace(30, 5)
print(replace)