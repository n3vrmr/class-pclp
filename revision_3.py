#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:13:47 2022

@author: Nevermore
"""

# Given a number 'n', asking a few questions
def odd_even(n):
    """Determines whether an integer 'n' is odd or even.
    """
    remain = n%2
    if remain == 0:
        print("n is an even number")
    else:
        print("n is an odd number")
    return n, remain
    
def listed_numbers(ns):
    """Determines whether the numbers in a given list are odd or even.
    """
    for n in ns:
        odd_even(n)
        print(n)

g = [820,8574,6457,643,365479,82176]
listed_numbers(g)

def main():
    print("Studying")
    
if __name__ == '__main__':
    odd_even(2)
    main()