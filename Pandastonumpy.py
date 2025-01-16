# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:07:52 2024

@author: HP
"""

import pandas as pd
# Specify the full path to the Excel file
file_path = r"C:\Users\HP\Basics\mark.xlsx"
df = pd.read_excel(file_path)

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