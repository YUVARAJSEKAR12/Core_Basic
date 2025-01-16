# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 05:52:39 2024

@author: HP
"""

import numpy as np
import pandas as pd


A=np.array([1497.55,165.55,7537.95,238.35,36.30,61.35,636.50])
B=np.array([672.80,183.60,8291.70,256.25,38.85,65.05,674.50])
C=np.array([11.70,10.90,10.00,7.51,7.02, 6.03,5.97])
Z=B-A
print("B-A value",Z)
X=A*C
print("A*C value",X)
Multiplyjustdialvalue=A[6]*C[6]
print("Multiply just dial value",Multiplyjustdialvalue)
companyname=np.array(['Polyplex Corpn','BLS International Se','National Standard I','Mirza International','Dhani Services','Wardwizard Innovation','Just Dial'])
slicedcompanyname=companyname[4:7]
print("sliced company name",slicedcompanyname)
AMIN=np.min(A)
BMIN=np.min(B)
CMIN=np.min(C)
AMINARRAY=np.array([AMIN])
BMINARRAY=np.array([BMIN])
CMINARRAY=np.array([CMIN])
print("A min value",AMIN)
print("B min value",BMIN)
print("C min value",CMIN)
AMAX= np.max(A)
BMAX= np.max(B)
CMAX= np.max(C)
AMAXARRAY=np.array([AMAX])
BMAXARRAY=np.array([BMAX])
CMAXARRAY=np.array([CMAX])
print("A max value",AMAX)
print("B max value",BMAX)
print("C max value",CMAX)
SORTA=np.sort(A)
SORTB=np.sort(B)
SORTC=np.sort(C)
print("sort of A",SORTA)
print("sort of B",SORTB)
print("sort of C",SORTC)
FLIPSORTA=np.flip(SORTA)
FLIPSORTB=np.flip(SORTB)
FLIPSORTC=np.flip(SORTC)
print("Reversed A",FLIPSORTA)
print("Reversed B",FLIPSORTB)
print("Reversed C",FLIPSORTC)
frame={"B-A value":Z, "A*C value":X, "Multiply just dial value":Multiplyjustdialvalue}
g=pd.DataFrame(frame)
print(g)
frame1={"A MIN ARRAY":AMINARRAY,"B MIN ARRAY":BMINARRAY,"C MIN ARRAY":CMINARRAY}
g1=pd.DataFrame(frame1)
print(g1)
frame2={"A MAX ARRAY":AMAXARRAY,"B MAX ARRAY":BMAXARRAY,"C MAX ARRAY":CMAXARRAY}
g2=pd.DataFrame(frame2)
print(g2)
frame3={"A SORT ARRAY":SORTA,"B SORT ARRAY":SORTB,"C SORT ARRAY":SORTC}
g3=pd.DataFrame(frame3)
print(g3)
frame4={"A FLIP ARRAY":FLIPSORTA,"B FLIP ARRAY":FLIPSORTB,"C FLIP ARRAY":FLIPSORTC}
g4=pd.DataFrame(frame4)
print(g4)