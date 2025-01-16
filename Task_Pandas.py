# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:17:24 2024

@author: HP
"""

import pandas as pd

file_path = r"C:\Users\HP\Basics\mark.xlsx"
df = pd.read_excel(file_path)

df =pd.read_excel('mark.xlsx')
arrN=df[['Name']].to_numpy().flatten()
arrM=df[['Math']].to_numpy().flatten()
arrP=df[['Phy']].to_numpy().flatten()
arrC=df[['Che']].to_numpy().flatten()
arrE=df[['Eng']].to_numpy().flatten()
arrB=df[['Bio']].to_numpy().flatten()
arrT=df[['Tamil']].to_numpy().flatten()
total=arrM+arrP+arrC+arrE+arrB+arrT
frame={"Name":arrN, "Total of all marks +":arrT}
dfn=pd.DataFrame(frame)
print(dfn)
dfn.to_excel("Filetest.xlsx",index = False)