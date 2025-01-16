# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:36:45 2024

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
csv_file = 'sales_data.csv'
df.to_csv(csv_file, index=False)
print(f"CSV file created: {csv_file}")
df_from_csv = pd.read_csv(csv_file)
print("\nData from CSV file:")
print(df_from_csv)


