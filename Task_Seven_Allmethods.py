# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 08:22:39 2024

@author: HP
"""

import pandas as pd

def incometax():
    df1=pd.read_excel("Income_Tax_Details.xlsx")
    print(df1)
    return df1
def stock_Register():
    df2=pd.read_excel("Stock_Register.xlsx")
    print(df2)
    return df2
def salary():
    df3=pd.read_excel("Salary_Details.xlsx")
    print(df3)
    return df3
def employee_Attendance():
    df4=pd.read_excel("Employee_Attendance.xlsx")
    print(df4)
    return df4
def consumables_Register():
    df5=pd.read_excel("Consumables_Register.xlsx")
    print(df5)
    return df5
def feedback_and_Customer_Details():
    df6=pd.read_excel("Feedback_and_Customer_Details.xlsx")
    print(df6)
    return df6
def sales_and_Profit():
    df7=pd.read_excel("Sales_and_Profit.xlsx")
    print(df7)
    return df7
c= input("Can I help you : ")
len=c.lower()
a=["could","you","provide","a","simple","explanation",
    "of","can","break","down","the","concept","for",
    "me","what","exactly","is","explain","how","does",
    "work","why","we","need","definition","tell","me",
    "about","describe","called","state","define","?",
    "get","i","?"]   
 
print("\ninput in lower case =",len)
wordsSplit=len.split()
print("\ninput in list Format=",wordsSplit)
filter=[x for x in wordsSplit if x.lower() not in a]
print("\nfiltered words = ",filter)
result = " ".join(filter)
print("\nKey word=", result)
expected1="incometax"
expected2="stockregister"
expected3="salary"
expected4="attendance"
expected5="consumables"
expected6="feedback"
expected7="sales"
if(result==expected1): incometax()
elif (result==expected2): stock_Register()
elif (result==expected3): salary()
elif (result==expected4): employee_Attendance()
elif (result==expected5): consumables_Register()
elif (result==expected6): feedback_and_Customer_Details()
elif (result==expected7): sales_and_Profit()
else:
    print("File not found ")

