# -*- coding: utf-8 -*-
"""
Created on Tue May 10 23:10:33 2022

@author: Nevermore
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def discount(self, percentage):
        self.price = self.price - (self.price*(percentage/100))
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('U$', ''))
        self._price = value
        
p1 = Product('AirJordans', 'U$750')
p1.discount(10)
print(p1.name, p1.price)

p2 = Product('AllStar', 'U$20')
p2.discount(35)
print(p2.name, p2.price)