# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:26:11 2024

@author: HP
"""
import numpy as np
import pandas as pd

company = ["Kolte-Patil Develope","Apcotex Industries L","Genus Power Infrastr","Rallis India","MCX","Mahindra CIE Auto"]

prevClose =[262.50,432.20,84.75,241.50,1509.35,356.70]

currentPrice =[307.85,466.85,91.10,258.05,1604.15,377.50]

prevClose_array = np.array(prevClose)
currentPrice_array = np.array(currentPrice)
company_array = np.array(company)

percentage_increase = ((currentPrice_array - prevClose_array) / prevClose_array) * 100

print(percentage_increase)
    
frame = {"Company":company_array,"Prev Close (Rs)":prevClose_array,"Current Price (Rs)":currentPrice_array,"% Change":percentage_increase}
g = pd.DataFrame(frame)
print(g)   
g.to_excel('output1.xlsx', index=False)
g.to_csv('file1.csv', index=False)
    
    
    
    