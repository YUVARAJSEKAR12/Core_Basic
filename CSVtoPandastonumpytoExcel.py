# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:11:37 2024

@author: HP
"""

import pandas as pd

csv_file = 'Sample_Data.csv'
df = pd.read_csv(csv_file)

raise_percentage = 0.10
df['new_salary'] = df['salary'] * (1 + raise_percentage)
excel_file = 'employee_data_with_new_salaries.xlsx'
df.to_excel(excel_file, index=False)

print(f"The updated data has been written to {excel_file}")