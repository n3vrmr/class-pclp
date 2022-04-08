# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:07:43 2022

@author: Nevermore
"""
# do NOT remove input line or WILL result in INFINITE LOOP
name = "Raven"
answer = False
while name == "Raven":
    print("\033[1;35;47mFiend from the Night's Plutonian shore!\033[0m")
    if not answer == True:
        name = input("\033[1;35;47mWhat is your name?\033[0m ")
        answer = True