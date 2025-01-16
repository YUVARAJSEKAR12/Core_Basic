# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 06:34:33 2024

@author: HP
"""
import pandas as pd
import numpy as np

file_path = r"C:\Users\HP\Basics\mark.xlsx"
df = pd.read_excel(file_path)
print(df)

q1=df.query('Math > 90')
print(" Math > 90\n",q1)

q3=df.query('Math > 90 and Phy >90 and Eng >70')
print(q3)

q4=df.query('Math > 90 and Phy >90 and Eng >70 and Che>90')
print(q4)

q5=df.query('Math == 90 or Phy ==90 or Eng ==80 or Che==90')
print(q5)

q5=df.query('Math == 91')
print(q5)

#file_path = r"C:\Users\HP\Basics\mark.csv"
#df = pd.read_excel(file_path)
#print(df)

# Create numpy arrays
a = np.array([11, 99, 303, 44, 55, 6])
b = np.array([1, 2, 3, 4, 5, 6])
c = a + b
d = np.array(["Abi", "Bala", "Coulins", "Dinesh", "Elger", "Ganesh"])

# Create a DataFrame
frame = {"Name": d, "A": a, "B": b, "C": c}
g = pd.DataFrame(frame)

# Display the DataFrame
print(g)

# Specify the file paths
excel_file_path = r'C:\Users\HP\Basics\TestOne.xlsx'
csv_file_path = r'C:\Users\HP\Basics\TestTwo.csv'

# Write the DataFrame to Excel and CSV files
#g.to_excel(excel_file_path, index=False)
#g.to_csv(csv_file_path, index=False)