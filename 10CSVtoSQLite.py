# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:43:35 2024

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


