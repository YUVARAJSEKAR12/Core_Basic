# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:28:37 2024

@author: HP
"""
import pandas as pd

data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Q1': [200, 300, 250, 400],
    'Q2': [220, 320, 275, 410],
    'Q3': [210, 310, 265, 420],
    'Q4': [240, 330, 280, 430]
}
df = pd.DataFrame(data)
excel_file = 'sales_data.xlsx'
df.to_excel(excel_file, index=False)
df_from_excel = pd.read_excel(excel_file)

print("\nData from Excel file:")
print(df_from_excel)

