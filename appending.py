# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:16:19 2022

@author: Nevermore
"""

names = []

go = True
while go:
    go = False
    name = input("Name: ")
    names.append(name)
    cont = input("\033[1;31;47mContinue? Reply Y for Yes or N for No.\033[0m ")
    if cont == "Y":
        go = True
    elif cont == "N":
        go = False

# Alphabetical
names.sort()
for indice,name in enumerate(names):
    print(indice,name)