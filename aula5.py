#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:15:45 2022

@author: nvrmr
"""

name = "Nevermore"
age = 22
age_days = 22*365.25

list_names = ["Nevermore", "Lenore", "Annabel Lee",
            "Poe"]
print("\033[1;31;47mSelecting the first element\033[0m")
name = list_names[0]
print(list_names[0])

print("\033[1;35;47mSelecting the second element\033[0m")
name = list_names[1]
print(name)

for name in list_names:
    print(name)
    
list_names.append("Raven")
print(list_names)
    
    
    
# dictionary
myDict = {"name": "Python", "age": 22}
print(myDict["name"])
print(myDict["age"])