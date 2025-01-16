# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:22:07 2024

@author: HP
"""

import pandas as pd
c= input("Enter the 1 for file 1 ,2 for file 2...")
if c=='1' or c=='file1' or c=='f1'or c=='one' or  c=='One' or c=='ONE' or c=='F1':
   df1=pd.read_excel("xlrandom1.xlsx")
   print(df1)
elif c=='2' or c=='file2'or c=='f2':
   df2=pd.read_excel("xlrandom2.xlsx")
   print(df2)
elif c=='3' or c=='file3'or c=='f3':
   df3=pd.read_excel("xlrandom3.xlsx")
   print(df3)
elif c=='4' or c=='file4'or c=='f4':
   df4=pd.read_excel("xlrandom4.xlsx")
   print(df4)
else:
    print("File not found ")