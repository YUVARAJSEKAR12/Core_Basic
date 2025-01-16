# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:58:59 2024

@author: HP
"""

import pandas as pd
c= input("Enter  1 for file 1 ,2 for file 2...")
if c=='1' :
   df1=pd.read_excel("Income_Tax_Details.xlsx")
   print(df1)
elif c=='2' :
   df2=pd.read_excel("Stock_Register.xlsx")
   print(df2)
elif c=='3' :
   df3=pd.read_excel("Salary_Details.xlsx")
   print(df3)
elif c=='4' :
   df4=pd.read_excel("Employee_Attendance.xlsx")
   print(df4)
elif c=='5' :
      df4=pd.read_excel("Consumables_Register.xlsx")
      print(df4)
elif c=='6' :
         df4=pd.read_excel("Feedback_and_Customer_Details.xlsx")
         print(df4)
elif c=='7' :
         df4=pd.read_excel("Sales_and_Profit.xlsx")
         print(df4)  
else:
    print("File not found ")