# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:44:11 2024

@author: HP
"""

import pandas as pd
import sqlite3

df = pd.read_excel("hr_data.xlsx")
database = "mark.sqlite"
conn = sqlite3.connect("hr_data.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)
conn.close()

df = pd.read_excel("Nuclearpower_generation_data.xlsx")
#database = "mark.sqlite"
conn = sqlite3.connect("Nuclearpower_generation_data.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)
conn.close()

df = pd.read_excel("sales11.xlsx")
#database = "mark.sqlite"
conn = sqlite3.connect("sales11.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)
conn.close()

df = pd.read_excel("diabetic_patients_data.xlsx")
#database = "mark.sqlite"
conn = sqlite3.connect("diabetic_patients_data.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)
conn.close()