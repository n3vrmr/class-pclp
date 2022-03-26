# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:02:20 2022

@author: Nevermore
"""

name = input("\033[1;35;47mWhat is your name?\033[0m ")
age = input("\033[1;31;47mHow old are you?\033[0m ")

age_days = int(age) * 365.25
employed = False

print(f"Hello, \033[1;35;47m{name}\033[0m! ")
print(f"You are \033[1;31;47m{age}\033[0m years old.")
print(f"In days, you are \033[1;32;40m{age_days}\033[0m days old. ")
print(f"Your employment status is {employed}. ")

list_names = ['Nevermore', 'Blood', 'Matheus']

print(list_names[0])
