# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:10:08 2024

@author: HP
"""

import numpy as np
import pandas as pd

A = np.array([1497.55,165.55,7537.95,238.35,36.30,61.35,636.50])
B = np.array([672.80,183.60,8291.70,256.25,38.85,65.05,674.50])
C= np.array([11.70,10.90,10.00,7.51,7.02,6.03,5.97])

print("Value of Array A= ",A)
print("Value of Array B= ",B)
print("Value of Array C=",C)


Z = B-A
print("Z=",Z)

X = A*C
print("X=",X)
print("X index", X[6])

jd = np.array(A[6] * C[6])
print("justdial", jd)

lastThree= np.array((A[4:],B[4:],C[4:]))
print(lastThree)

minA = np.min(A)
minB = np.min(B)
minC = np.min(C)
print("A min ",minA)
print("B min ",minB)      
print("C min ", minC)     

maxA = np.max(A)
maxB = np.max(B)
maxC = np.max(C)
print("A max ",maxA)
print("B max ",maxB)      
print("C max ",maxC)  

meanA = np.mean(A)
meanB = np.mean(B)
meanC = np.mean(C)
print("A mean ",meanA)
print("B mean ",meanB)      
print("C mean ",meanC) 

reverseA= np.flip(A)
reverseB= np.flip(B)
reverseC= np.flip(C)
print("A rev ",reverseA)
print("B rev ",reverseB)      
print("C rev ",reverseC)

sortA= np.sort(A)
sortB= np.sort(B)
sortC= np.sort(C)
print("C sort ",sortA)
print("C sort ",sortB)
print("C sort ",sortC)

frame = {"B-A":Z,"A*C":X,"JustDial":jd,
         "MinA":minA,"MinB":minB,"MinC":minC,
         "MaxA":maxA,"MaxB":maxB,"MaxC":maxC,
         "ReverseA":reverseA,"ReverseB":reverseB,"ReverseC":reverseC,
         "SortA":sortA,"SortB":sortB,"SortC":sortB}
g= pd.DataFrame(frame)
print(g)
g.to_excel("Data_One.xlsx",index=False)



