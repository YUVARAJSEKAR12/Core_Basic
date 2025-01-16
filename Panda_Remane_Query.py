# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:52:11 2024

@author: HP
"""


import pandas as pd
# Specify the full path to the Excel file
file_path = r"C:\Users\HP\Basics\mark.xlsx"
df = pd.read_excel(file_path)
print(df)

df.rename(columns={'Math': 'Mat'}, inplace=True)
h=df.head(1)
print(h)


df.rename(columns={'Mat': 'Math','Phy':'P'}, inplace=True)
h=df.head(1)
print(h)

df.rename(columns={'P': 'Phy'}, inplace=True)
h=df.head(1)
print(h)

q1=df.query('Math > 90')
print(" Math > 90\n",q1)


q2=df.query('Math > 90 and Phy >90')
print(q2)

q3=df.query('Math > 90 and Phy >90 and Eng >90')
print(q3)

q4=df.query('Math > 90 and Phy >90 and Eng >90 and Che>90')
print(q4)

q5=df.query('Math == 90 or Phy ==90 or Eng ==90 or Che==90')
print(q5)

q5=df.query('Math == 91')
print(q5)