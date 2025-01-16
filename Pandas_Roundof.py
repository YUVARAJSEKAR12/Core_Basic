# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:18:20 2024

@author: HP
"""

import pandas as pd

df =pd.read_excel('mark.xlsx')
c=df.round(0)
print(c)