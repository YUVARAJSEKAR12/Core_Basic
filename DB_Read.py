# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:41:46 2024

@author: HP
"""

# read DB
import pandas as pd
import sqlite3 as db
con = db.connect('mark.sqlite')
df = pd.read_sql_query("SELECT min(Math)  FROM Users", con)
print(df)
g = pd.DataFrame({df},index=[0])
print(g)
g.to_excel("Min_Excel",index=False)
con.commit()
con.close()

