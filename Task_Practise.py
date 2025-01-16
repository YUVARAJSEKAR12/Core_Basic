# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 03:51:25 2024

@author: HP
"""

import pandas as pd
import sqlite3

df = pd.read_excel("sales11.xlsx")
#database = "mark.sqlite"
conn = sqlite3.connect("sales11.sqlite")
df.to_sql(name='Sales',con=conn,if_exists='replace',index=False)