#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:14:36 2022

@author: nvrmr
"""

print("\033[1;30;47mHello, world!\033[0m")

name = input("\033[1;35;47mWhat is your name?\033[0m ")
age = int(input("\033[1;34;47mHow old are you?\033[0m "))

age_days = int(age) * 365.25
employed = False

print(f"Hello, \033[1;35;47m{name}\033[0m! ")
print(f"You are \033[1;34;47m{age}\033[0m years old. ")
print(f"In days, you are \033[1;32;40m{age_days}\033[0m days old. ")
print(f"Your employment status is \033[1;31;40m{employed}\033[0m. ")