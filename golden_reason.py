# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:17:09 2022

@author: Nevermore
"""

def golden(x):
    x >= 2
    values = [0,1]
    for i in range(2,x):
        values.append(values[i-1] + values[i-2])
        reason = max(values)/values[i-1]
    return reason

def main():
    print("Hope this works")

if __name__ == '__main__':
    main()
    reason = golden(1000)