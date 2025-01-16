# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:54:34 2024

@author: HP
"""

import pandas as pd
c= input("Enter  1 for file 1 ,2 for file 2...")
if c=='1' :
   df1=pd.read_excel("xlrandom1.xlsx")
   print(df1)
elif c=='2' :
   df2=pd.read_excel("xlrandom2.xlsx")
   print(df2)
elif c=='3' :
   df3=pd.read_excel("xlrandom3.xlsx")
   print(df3)
elif c=='4' :
   df4=pd.read_excel("xlrandom4.xlsx")
   print(df4)
else:
    print("File not found ")