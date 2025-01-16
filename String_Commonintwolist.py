# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:07:51 2024

@author: HP
"""

a = ['apple', 'banana', 'cherry']   # list of words to exclude (case insensitive)
b = ['Apple', 'orange', 'Banana', 'grape', 'Cherry']
filtered_words = [word for word in b if word.lower() not in a]
print(filtered_words)