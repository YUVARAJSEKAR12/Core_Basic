# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:42:25 2024

@author: HP
"""
import numpy as np
import pandas as pd

#1.	Assign a variable “Company” and print the above Company name
company = ["Kolte-Patil Develope","Apcotex Industries L","Genus Power Infrastr","Rallis India","MCX","Mahindra CIE Auto"]

print(company)
#2.	Find length of the Company
size = len(company)
print(size)
#5.	Insert a Company name “TCS” in to a list company 
add= ["TCS"]
company.extend(add)
print(company)
#6.	Delete MCX from company
company.remove("MCX")
print(company)

#3.	Form a list for previous close and current price 
prevClose =["262.50","432.20","84.75","241.50","1509.35","356.70"]
print(prevClose)
#4.	Remove the value 1509.35 from prev close
prevClose.remove("1509.35")
print(prevClose)

#3.	Form a list for previous close and current price 
currentPrice =["307.85","466.85","91.10","258.05","1604.15","377.50"]
print(currentPrice)

prevClose =[262.50,432.20,84.75,241.50,1509.35,356.70]

currentPrice =[307.85,466.85,91.10,258.05,1604.15,377.50]

prevClose_array = np.array(prevClose)
currentPrice_array = np.array(currentPrice)

percentage_increase = ((currentPrice_array - prevClose_array) / prevClose_array) * 100

print(percentage_increase)

for old, new, percentage in zip(prevClose, currentPrice, percentage_increase):
    print(f"Old Value: {old}, New Value: {new}, Percentage Increase: {percentage:.2f}%")
    
    
    
    