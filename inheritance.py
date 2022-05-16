# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:56:55 2022

@author: Nevermore
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nameclass = self.__class__.__name__
    
    def speak(self):
        print(f"{self.nameclass} speaking...")

class Client(Person):
    def buy(self):
        print(f"{self.nameclass} buying...")
        
class Student(Person):
    def study(self):
        print(f"{self.nameclass} studying...")

c1 = Client("Henrique", 35)
print(c1.name)
c1.speak()
c1.buy()

a1 = Student("Ana", 23)
print(a1.name)
a1.speak()
a1.study()