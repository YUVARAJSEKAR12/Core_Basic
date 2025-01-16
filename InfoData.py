# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:43:50 2024

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

