# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:34:32 2024

@author: HP
"""

import pandas as pd
import sqlite3

file_path = r"C:\Users\HP\Basics\mark.xlsx"
df = pd.read_excel(file_path)
#database = "mark.sqlite"
conn = sqlite3.connect("mark.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)