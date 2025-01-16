# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:57:42 2024

@author: HP
"""
import Levenshtein as lev

Str1 = "Good "

Str2 = "Hi Good Morning"


Distance = lev.distance(Str1.lower(),Str2.lower()),

print(Distance)