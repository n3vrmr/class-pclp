#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:15:44 2022

@author: Aluno07
"""
import random as rd

test = {}

test["first"] = rd.randint(1,12)
test["second"] = rd.randint(1,12)

print(test)

# test["first"] = test.get("first") + 4
# print(test)

def add(key):
    test[f"{key}"] = test.get(f"{key}") + 4
    print(test)
    return test

add("first")

class Pessoa:
    def __init__(self, name, data={}):
        self.name = name
        self.data = data
        self.insert_data()
        healthy = BloodPressure()
        self.healthy = healthy
        return
    
    def insert_data(self):
        self.data = {}
        self.data["age"] = rd.randint(18,34)
        self.data["id"] = rd.randint(10000,99999)
        self.data["temperature"] = 36 + rd.random()
        self.data["blood pressure"] = BloodPressure.blood_pressure(self)
        return self.data
    
    def change_data(self):
        self.data["age"] = self.data.get("age") + 2
        self.data["temperature"] = self.data.get("temperature") + rd.random()
        return self.data
    
    def physical_activity(self):
        pa = True
        while pa:
            pa = False
            self.data["temperature"] = self.data.get("temperature") + 2 * rd.random()
            self.data["blood pressure"] = self.data.get("blood pressure") + rd.randint(15,30)
            print(self.name,self.data)
        return self.data
    
class BloodPressure:
    # def __init__(self):
    #     self.healthy = input("Healthy? ")
    #     return
    
    def blood_pressure(self):
        self.healthy = input("Healthy? ")
        if "y" in self.healthy:
            self.pressure = rd.randint(110,120)
        else:
            self.pressure = rd.randint(121,139)
        return self.pressure
    
    

p1 = Pessoa("Vini")
print(p1.name,p1.data)
p1.change_data()
print(p1.name,p1.data)
p1.physical_activity()
print(p1.name,p1.data)