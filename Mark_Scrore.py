# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:50:27 2024

@author: HP
"""

score1 = int(input("Enter score1: "))
if score1 > 90:
    print("Student grade is A")
elif score1 >= 80 and score1 <= 89:
    print("Student grade is B")
elif score1 >= 70 and score1 <= 79:
    print("Student grade is C")
elif score1 >= 60 and score1 <= 69:
    print("Student grade is D")
else:
    print("Student grade is F")