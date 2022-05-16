# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:35:16 2022

@author: Nevermore
"""

class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adresses = []
        
    def insert_address(self, city, state):
        self.adresses.append(Address(city, state))
    
    def lista_addresses(self):
        for address in self.adresses:
            print(address.city, address.state)
    
    def __del__(self):
        print(f"{self.name} has been erased.")
        
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
    def __del__(self):
        print(f"{self.city} / {self.state} have been erased.")