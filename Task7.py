# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 05:04:44 2024

@author: HP
"""

import numpy as np
import pandas as pd
companyname=np.array(["Kirloskar Pneumatic","DCB Bank","Thermax","Laurus Labs","Jammu & Kashmir Bank"])
previousclose=np.array([1497.55,165.55,7537.95,238.35,36.30])
currentprice=np.array([672.80,183.60,8291.70,256.25,38.85])
change=np.array([11.70,10.90,10.00,7.51,7.02])


frame={ "CompanyName":companyname, "PreviousClose":previousclose, "CurrentPrice":currentprice, "Change":change}
g=pd.DataFrame(frame)
print(g)





