# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:42:45 2024

@author: HP
"""

a = 3000
b = 4000
if b > a:
  print("b is greater than a")


#error sim
a = 33
b = 200 
if b>a:
print("b is greater than a") # you will get an error


#ELSE IF
a = 433
b = 433
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("else ")