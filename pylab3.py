# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:14:50 2022

@author: nvrmr
"""

prof = {"name":"Álvaro", "age":33, "temperature":36.5, "has_cats":True}


if prof["temperature"] < 38:
    print("Álvaro peut entrer.")
if prof["has_cats"] == True:
    print("\033[1;34;47mProfesseur Álvaro a trois chats.\033[0m")
    
print(prof["age"])
print(__name__)

# sorting dictionaries inside a list
# for <variable> in <list>:
    # <list>.append(<variable>["<key>"])
# print(sorted(<list>))
