# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:15:39 2024

@author: HP
"""

a = ["what", "how", "why","is","in","your"]#only lower case
ip= input("Enter your sentence: ")
l=ip.lower()
print("\ninput in lower case =",l)
# Split the input string into individual words
b = l.split()
print("\ninput in list Format=",b)

# Create a new list without the words to remove
filter = [word for word in b if word.lower() not in a]
print("\nfiltered words=",filter)
# Join the filtered words back together
result = " ".join(filter)
print("\nKey word=", result)