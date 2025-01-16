# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:38:49 2024

@author: HP
"""

import pandas as pd

def file1():
    df1=pd.read_excel("Income_Tax_Details.xlsx")
    print(df1)
    return df1
def file2():
    df2=pd.read_excel("Stock_Register.xlsx")
    print(df2)
    return df2
def file3():
    df3=pd.read_excel("xlrandom3.xlsx")
    print(df3)
    return df3
def file4():
    df4=pd.read_excel("Employee_Attendance.xlsx")
    print(df4)
    return df4
def file5():
    df5=pd.read_excel("Consumables_Register.xlsx")
    print(df5)
    return df5
def file6():
    df6=pd.read_excel("Feedback_and_Customer_Details.xlsx")
    print(df6)
    return df6
def file7():
    df7=pd.read_excel("Sales_and_Profit.xlsx")
    print(df7)
    return df7
    df4=pd.read_excel("xlrandom4.xls
    return df4
c= input("Enter the file you want to read ")
if c=='1' or c=='file1' or c=='f1':
   a=file1()
elif c=='2' or c=='file2'or c=='f2':
   b=file2()
elif c=='3' or c=='file3'or c=='f3':
   c=file3()
elif c=='4' or c=='file4'or c=='f4':
   d=file4()
elif c=='5' or c=='file5'or c=='f5':
   d=file5()
elif c=='6' or c=='file6'or c=='f6':
   d=file6()
elif c=='7' or c=='file7'or c=='f7':
   d=file7()   
else:
    print("File not found ")

