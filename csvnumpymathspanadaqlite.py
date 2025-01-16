# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:22:52 2024

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:15:55 2024

@author: HP
"""

import pandas as pd
import numpy as np
import sqlite3

# Step 1: Read the CSV file into a pandas DataFrame
csv_file = 'Sample_Data.csv'
df = pd.read_csv(csv_file)

# Step 2: Convert the 'salary' column to a NumPy array and apply a 10% raise
# Convert salary to NumPy array
salaries = df['salary'].to_numpy()

# Apply a 10% raise using NumPy operations
new_salaries = salaries * 1.10  # 10% raise

# Step 3: Add the modified salaries back to the DataFrame
df['new_salary'] = new_salaries

# Step 4: Create an SQLite database and insert the data
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Step 5: Create the employees table (if it doesn't exist already)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        salary INTEGER,
        new_salary REAL
    )
''')

# Step 6: Insert the DataFrame into the SQLite database
# Use pandas to_sql method to insert the data into the table
df.to_sql('employees', conn, if_exists='replace', index=False)

# Step 7: Commit the changes and close the connection
conn.commit()

# Verify the data was inserted by querying the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Print the rows in the database
print("Employee Data in SQLite Database:")
for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()