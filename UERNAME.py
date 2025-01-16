# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:48:35 2024

@author: HP
"""

# Define user ID and password
user_id = "Yuvaraj"
password = "Muru122340"

# Get user input for user ID and password
input_user_id = input("Enter user ID: ")
input_password = input("Enter password: ")

# Check if the user ID and password are correct
if input_user_id == user_id and input_password == password:
    # Give access to the module
    print("Access granted. Welcome to the module!")
else:
    # Deny access
    print("Access denied. Incorrect user ID or password.")