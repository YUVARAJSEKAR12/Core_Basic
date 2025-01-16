# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:34:35 2024

@author: HP
"""

import numpy as np

x = np.array([12, 38,65,87,67])

ra= np.flip(x)
print(ra)


# sorting a array
import numpy as np

arr = np.array([0, 12, 1, 3, 4, 5, 6])
print("Original array:")
print(arr)
arr1 = np.sort(arr)
print(arr1)
ra= np.flip(arr1)
print(ra)