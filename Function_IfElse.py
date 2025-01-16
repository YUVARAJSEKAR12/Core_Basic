# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:22:01 2024

@author: HP
"""

import pandas as pd
def file1():
    df1=pd.read_excel("xlrandom1.xlsx")
    print(df1)
    return df1
def file2():
    df2=pd.read_excel("xlrandom2.xlsx")
    print(df2)
    return df2
def file3():
    df3=pd.read_excel("xlrandom3.xlsx")
    print(df3)
    return df3
def file4():
    df4=pd.read_excel("xlrandom4.xlsx")
    print(df4)
    return df4
c= input("Enter the file you want to read")
if c=='1' or c=='file1' or c=='f1':
   a=file1()
elif c=='2' or c=='file2'or c=='f2':
   b=file2()
elif c=='3' or c=='file3'or c=='f3':
   c=file3()
elif c=='4' or c=='file4'or c=='f4':
   d=file4()
else:
    print("File not found ")