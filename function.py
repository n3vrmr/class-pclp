#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:33:50 2022

@author: nvrmr
"""
import random

def sum_numbers(a,b):
    """
    Sums two values
    ----
    Arguments:
        a: first value
        b: second value
    """
    return a + b

def main():
    print(sum_numbers(1,1))
    
print(__name__)

if __name__ == '__main__':
    main()
    print(random.random())

def coin_toss():
    result = random.randint(0,1)
    if result == 0:
        print("Heads")
        return "heads"
    else:
        print("Tails")
        return "tails"
        
def heads_or_tails():
    result = input("Heads or tails? ")
    result = result.lower().strip()
    adversary = coin_toss()
    if result == adversary:
        print("You win!")
    else:
        print("You lose! Better luck next time!")
    
    
def roll():
    d20 = random.randint(1,20)
    if d20 == 20:
        print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
    elif d20 == 1:
        print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
        
heads_or_tails()
roll()
# print(help(sum_numbers))
