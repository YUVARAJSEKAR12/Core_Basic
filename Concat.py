# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:37:43 2024

@author: HP
"""

#Concatenate
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)