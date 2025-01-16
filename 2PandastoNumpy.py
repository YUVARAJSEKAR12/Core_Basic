# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:58:24 2024

@author: HP
"""

import pandas as pd
import numpy as np
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Q1': [200, 300, 250, 400],
    'Q2': [220, 320, 275, 410],
    'Q3': [210, 310, 265, 420],
    'Q4': [240, 330, 280, 430]
}

df = pd.DataFrame(data)
series = df['Q1']
print("Pandas DataFrame:")
print(df)
df_numpy = df.to_numpy()  # or df.values
print("\nDataFrame as NumPy Array:")
print(df_numpy)