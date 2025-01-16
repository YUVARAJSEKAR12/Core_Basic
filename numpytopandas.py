# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 06:32:05 2024

@author: HP
"""

import numpy as np
import pandas as pd


a = np.array([1,2,3,4,5,6])
b = np.array([2,1,1,1,12,9])
c = a+b;
print(a)
print(b)
print(c)

df= pd.DataFrame({"A":a,"B":b,"C":c})
print(df)

df = pd.Series(a)
print(df)
