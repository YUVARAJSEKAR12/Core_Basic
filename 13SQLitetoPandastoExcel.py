# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:04:42 2024

@author: HP
"""

import pandas as pd
import sqlite3 as db
df = pd.read_csv('mark.csv')
con = db.connect('mark.sqlite')
df = pd.read_sql_query("SELECT * FROM Users", con)
print(df)
con.commit()
con.close()
g = pd.DataFrame(df)
print(g)
g.to_excel('output1.xlsx', index=False)