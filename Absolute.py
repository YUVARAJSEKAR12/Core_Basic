# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:42:21 2024

@author: HP
"""

import numpy as np

arr = np.array([-1, -2, 1, 2, +3, -4])

newarr = np.absolute(arr)#polarity will be removed

print(newarr)