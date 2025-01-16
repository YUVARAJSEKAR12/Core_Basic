# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:49:39 2024

@author: HP
"""

import numpy as np
arr = np.array([41.25, 42.32, 43.65, 44.9999])
arr1 = np.around(arr, 0)
print(arr1)


import numpy as np
arr = np.array([41.25, 42.9, 43.25, 44])
arr1 = np.ceil([arr])
arr2=np.floor([arr])
print("Ceil=",arr1)
print("Floor=",arr2)