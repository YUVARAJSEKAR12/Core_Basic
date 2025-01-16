# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:53:46 2024

@author: HP
"""

import numpy as np

companyname=np.array(['Kirloskar Pneumatic','DCB Bank','Thermax','Laurus Labs','Jammu & Kashmir Bank'])
previousclose=np.array([1,337.00,110.25,5,178.05,446.00,93.85])
currentprice=np.array([1,467.60,116.35,5,435.00,465.00,97.70])
change=np.array([9.77,5.53,4.96,4.26,4.10])
print("companyname",companyname)
print("previousclose",previousclose)
min=np.min([previousclose])
max=np.max([currentprice])
mean=np.mean(previousclose)
print("previous closing minimum value",min)
print("previous closing maximum value",max)
print("previous average value",max)
print("current price",currentprice)
currentpricemin=np.min([currentprice])
currentpricemax=np.max([currentprice])
currentpricemean=np.mean(currentprice)
print("current price minimum value",currentpricemin)
print("current price maximum value",currentpricemax)
print("current price value",currentpricemean)
ten=currentprice*10/100
fifteen=currentprice*15/100
twenty=currentprice*20/100
tenvalue=currentprice+ten
fifteenvalue=currentprice+fifteen
twentyvalue=currentprice+twenty
print("current price 10 increment",tenvalue)
print("current price 15 increment",fifteenvalue)
print("current price 20 increment",twentyvalue)
