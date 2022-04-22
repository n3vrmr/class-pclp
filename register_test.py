# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:03:25 2022

@author: Nevermore
"""

users = []

go = True
while go:
    go = False
    user = {}
    user["name"] = input("Name: ")
    user["age"] = int(input("Age: "))
    user["registry"] = int(input("Registry number: "))
    user["major"] = input("Major: ")
    users.append(user)
    cont = input("\033[1;31;47mContinue? Reply Y for Yes or N for No.\033[0m ")
    cont = cont.lower().strip()
    if cont == "Y":
       go = True
    elif cont == "N":
       go = False

# print(len(users))
