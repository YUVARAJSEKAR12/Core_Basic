# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:10:34 2024

@author: HP
"""

import numpy as np
import pandas as pd

X = np.array([120,140,160,180,190])
Y = np.array([20,40,60,80,90])
Z = np.array([125,145,165,185,195])

A = X+Y
print (A)

B = X-Y
print (B)

C = X+Z
print(C)

D = Y+Z
print(D)

frame={"X":X, "Y":Y, "Z":Z, "X+Y":A,"X-Y":B,"X+Z":C,"Y+Z":D}
g=pd.DataFrame(frame)
print(g)

g.to_excel('output2.xlsx', index=False)
g.to_csv('file2.csv', index=False)
