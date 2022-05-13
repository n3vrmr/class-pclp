# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:42:45 2022

@author: Nevermore
"""

class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__tool = None
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, tool):
        self.__tool = tool
    
class Caneta:
    def __init__(self, marca):
        self.__marca = marca
        
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print("Caneta está escrevendo...")
    
class TypeWriter:
    def escrever(self):
        print("Máquina está escrevendo...")