# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:44:46 2024

@author: HP
"""

import numpy as np

arr = np.array([0,1, 2, 3, 4, 5, 6, 7])
x=arr[2:4]
print(x)
# 4: it will split and start from 4th index and print the remaining items in forward
y=arr[4:]
print(y)
# 4: it will split and start from 4th index and print the remaining items in backwardard
z=arr[:4]
print(z)


#Array size

b = np.array([1, 2, 3, 4, 5])
x=b.size
print(x)