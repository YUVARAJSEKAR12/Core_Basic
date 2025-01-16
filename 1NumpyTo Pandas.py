# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:56:54 2024

@author: HP
"""
import numpy as np
import pandas as pd


np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(np_array, columns=['A', 'B', 'C'])

print(df)
