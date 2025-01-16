# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:35:35 2024

@author: HP
"""

#1.	Assign a variable “Squad” and print the above players name
Squad =["Rohit Sharma (C)","Shubman Gill","Ishan Kishan"
        ,"Virat Kohli","Shreyas Iyer","Suryakumar Yadav","KS Bharat (wk)"
        ,"Hardik Pandya (vc)", 
        "Washington Sundar",
        "Shahbaz Ahmed", "Shardul Thakur", 
        "Yuzvendra Chahal", "Kuldeep Yadav",
        "Mohd. Shami","Mohd. Siraj", "Umran Malik"]
print(Squad)

#2.	Find length of the squad
size =len(Squad)
print(size)

# 3.	Print First 11 players name
eleven= Squad[0:11]
size=len(eleven)
print(eleven)
print(size)

#4.	Print captain name alone 
captain = Squad[0]
print(captain)

#5.	Print First 4 players name
fourplayer = Squad[0:4]
print(fourplayer)

#6.	Print 5th player name
fifthplayer = Squad[4]
print(fifthplayer)

#7.	Print last 4 player name

lastfour= Squad[12:]
print(lastfour)

#8.	Insert Dhoni name to squad 
add = ["Dhoni"]
Squad.extend(add)
print(Squad)

