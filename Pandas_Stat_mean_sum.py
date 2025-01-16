# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:15:37 2024

@author: HP
"""

import pandas as pd
df =pd.read_excel('mark.xlsx')
df1 = df[["Bio","Phy","Math","Tamil","Eng"]]
s=df1.sum()
print(s)


import pandas as pd
df =pd.read_excel('mark.xlsx')
df1 = df[["Bio","Phy","Math","Tamil","Eng"]]
m=df1.mean()
print(m)