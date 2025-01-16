# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:48:34 2024

@author: HP
"""

age = float(input("Enter the age ="));
if age>=0 and age<=2:
  print("Based on age falls under infant category")
elif age>=3  and age<=12:
  print("Based on age falls under child category")
elif age>=13  and age<=19:
  print("Based on age falls under teenager category")
elif age>=20  and age<=59:
  print("Based on age falls under adult category")
else:
  print("Based on age falls under senior citizen category")