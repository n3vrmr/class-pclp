# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:12:06 2022

@author: Nevermore
"""
import random
import numpy as np

def roll_d2():
    """ Rolls a two sided die (coin toss)
    
    """
    d2 = random.randint(1,2)
    if d2 == 1:
        print("1")
        return "1"
    else:
        print("2")
        return "2"

def roll_d3():
    """ Rolls a three sided die.
    
    """
    d3 = random.randint(1,3)
    if d3 == 1:
        print("1")
        return "1"
    elif d3 == 2:
        print("2")
        return "2"
    else:
        print ("3")
        return "3"

def roll_d4():
    """ Rolls a four sided die.

    """
    d4 = random.randint(1,4)
    if d4 == 1:
        print("1")
        return "1"
    elif d4 == 2:
        print("2")
        return "2"
    elif d4 == 3:
        print ("3")
        return "3"
    else:
        print("4")
        return "4"

def roll_d6():
    """ Rolls a six sided die
    
    """
    d6 = random.randint(1,6)
    if d6 == 1:
        print("1")
        return "1"
    elif d6 == 2:
        print("2")
        return "2"
    elif d6 == 3:
        print ("3")
        return "3"
    elif d6 == 4:
        print("4")
        return "4"
    elif d6 == 5:
        print("5")
        return "5"
    else:
        print("6")
        return "6"

def roll_d8():
    """ Rolls an eight sided die.
    
    """
    d8 = random.randint(1,8)
    if d8 == 1:
        print("1")
        return "1"
    elif d8 == 2:
        print("2")
        return "2"
    elif d8 == 3:
        print ("3")
        return "3"
    elif d8 == 4:
        print("4")
        return "4"
    elif d8 == 5:
        print("5")
        return "5"
    elif d8 == 6:
        print("6")
        return "6"
    elif d8 == 7:
        print("7")
        return "7"
    else:
        print("8")
        return "8"

def roll_d10():
    """ Rolls a ten sided die.
    
    """
    d10 = random.randint(1,10)
    if d10 == 1:
        print("1")
        return "1"
    elif d10 == 2:
        print("2")
        return "2"
    elif d10 == 3:
        print ("3")
        return "3"
    elif d10 == 4:
        print("4")
        return "4"
    elif d10 == 5:
        print("5")
        return "5"
    elif d10 == 6:
        print("6")
        return "6"
    elif d10 == 7:
        print("7")
        return "7"
    elif d10 == 8:
        print("8")
        return "8"
    elif d10 == 9:
        print("9")
        return "9"
    else:
        print("10")
        return "10"
    
def roll_d12():
    """ Rolls a twelve sided die.
    
    """
    d12 = random.randint(1,12)
    if d12 == 1:
        print("1")
        return "1"
    elif d12 == 2:
        print("2")
        return "2"
    elif d12 == 3:
        print ("3")
        return "3"
    elif d12 == 4:
        print("4")
        return "4"
    elif d12 == 5:
        print("5")
        return "5"
    elif d12 == 6:
        print("6")
        return "6"
    elif d12 == 7:
        print("7")
        return "7"
    elif d12 == 8:
        print("8")
        return "8"
    elif d12 == 9:
        print("9")
        return "9"
    elif d12 == 10:
        print("10")
        return "10"
    elif d12 == 11:
        print("11")
        return "11"
    else:
        print("12")
        return "12"
    
def roll_d20():
    """ Rolls a 20 sided die.
    
    """
    d20 = random.randint(1,20)
    if d20 == 1:
        print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
        return "1"
    elif d20 == 2:
        print("2")
        return "2"
    elif d20 == 3:
        print ("3")
        return "3"
    elif d20 == 4:
        print("4")
        return "4"
    elif d20 == 5:
        print("5")
        return "5"
    elif d20 == 6:
        print("6")
        return "6"
    elif d20 == 7:
        print("7")
        return "7"
    elif d20 == 8:
        print("8")
        return "8"
    elif d20 == 9:
        print("9")
        return "9"
    elif d20 == 10:
        print("10")
        return "10"
    elif d20 == 11:
        print("11")
        return "11"
    elif d20 == 12:
        print("12")
        return "12"
    elif d20 == 13:
        print("13")
        return "13"
    elif d20 == 14:
        print("14")
        return "14"
    elif d20 == 15:
        print("15")
        return "15"
    elif d20 == 16:
        print("16")
        return "16"
    elif d20 == 17:
        print("17")
        return "17"
    elif d20 == 18:
        print("18")
        return "18"
    elif d20 == 19:
        print("19")
        return "19"
    else:
        print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
        return "20"
    
def roll_d100():
    """ Rolls a percentile die.
    
    """
    d100 = random.random()*100
    print(np.round(d100,0))
    
roll_d2()
roll_d3()
roll_d4()
roll_d6()
roll_d8()
roll_d10()
roll_d12()
roll_d20()
roll_d100()

def main():
    if __name__ == '__main__':
        print("Take a chance, roll the dice!")
        
main()