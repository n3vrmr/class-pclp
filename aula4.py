#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 08:25:25 2022

@author: nvrmr
"""

myList = ['Descartes', 'Rousseau', 'Dumas', 'Montesquieu', 'Zola']

# Loops and indexing
for name in myList:
    print(name)
    
# Enumerate function
for indice,name in enumerate(myList):
    print(indice,name)
    if name == "Dumas":
        myList[indice] = indice
    else:
        print("Pas Dumas")
print(myList)