# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:54:33 2024

@author: HP
"""

import pandas as pd

df = pd.read_excel("mark.xlsx")

col = df[["Name","Phy"]]
print(col)

col.to_excel("File_read1.xlsx",index = False)