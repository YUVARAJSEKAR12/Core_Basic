# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:05:54 2024

@author: HP
"""
import numpy as np

prevClose =[262.50,432.20,84.75,241.50,1509.35,356.70]

currentPrice =[307.85,466.85,91.10,258.05,1604.15,377.50]

prevClose_array = np.array(prevClose)
currentPrice_array = np.array(currentPrice)

percentage_increase = ((currentPrice_array - prevClose_array) / prevClose_array) * 100

print(percentage_increase)

for old, new, percentage in zip(prevClose, currentPrice, percentage_increase):
    print(f"Old Value: {old}, New Value: {new}, Percentage Increase: {percentage:.2f}%")