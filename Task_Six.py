# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:25:50 2024

@author: HP
"""

   
a=["simple","can","break","down","explanation","of""could","you","provide","a","the","concept","for","me","what","exactly","is","explain","how","does","work","why","we","called","state","define","?""need","definition","tell","me","about","describe"]

inp=input("Enter your sentence: ")
len=inp.lower()
print("\ninput in lower case =",len)
#Split the string into individual words
wordsSplit=len.split()
print("\ninput in list Format=",wordsSplit)
#Create new list without the words to remove
filter=[wordsSplit for wordsSplit in wordsSplit if wordsSplit.lower() not in a]
print("\nfiltered words = ",filter)
# Join the filtered words back together
result = " ".join(filter)
print("\nKey word=", result)

