# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:49:14 2024

@author: HP
"""

weight = float(input("Enter the person weight ="));
if weight<=18.5:
  print("Based on weight falls under Underweight category")
elif weight>=18.5  and weight<=24.9:
  print("Based on weight falls under Normal weight")
elif weight>=25  and weight<=29.9:
  print("Based on weight falls under Overweight category")
else:
  print("Based on weight falls under Obese category")