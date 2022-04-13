#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:52:33 2022

@author: nvrmr
"""

name = "Chem"; age = 22; temperature_celsius = 36.5; has_cats = False
my_list = ['Mat',
           'Raven',
           'Lenore',
           'Annabel Lee',
           'Blood',
           'Nevermore']

friends_list = ['Gurjas',
                'Cabeçote',
                'Anão',
                'Big Milk']

# address = input("Address: ")

my_dict = {'name1': 'Matheus',
           'has_dogs': True}

student = {'name2':'M',
           'major':'Marketing',
           'RA':78}

# Flux Control
for friend in friends_list:
    print(friend)
    if friend == "Cabeçote":
        print("Happy bday!")
    else:
        print("Hi!")

print("\033[1;31;47mHello, world!\033[0m")
print("\033[1;31;47mWelcome to Python Lab\033[0m")