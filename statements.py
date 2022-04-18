# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:37:07 2022

@author: Nevermore
"""
# change the values of variables 'a' and 'b' to see the changes in the code

a = int(input("Choose an int value for a: "))
b = int(input("Choose an int value for b: "))
c = [0, 5, 10, 15]
d = [1, 5, 25, 125]
if a<10 and a>2:
    print("a is a value between 2 and 10")
if a<6 or a>6:
    print("this information is useless")
if not(a<10 and a>2):
    print("this is the opposite of the first statement")
if a is b:
    print("the two values are the same")
if a is not b:
    print ("the two values are different")
if a in c:
    print("value 'a' is a part of this sequence")
if b not in d:
    print("value 'b' is not a part of this sequence")
