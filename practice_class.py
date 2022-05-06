# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:35:05 2022

@author: Nevermore
"""

class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo.")
            return
        
        if self.falando:
            print(f"{self.nome} já está falando sobre {assunto}.")
            return
        
        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True
    
    def para_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        
        if self.falando:
            self.comendo = False
            print(f"{self.nome} parou de falar.")
            return
        
    def metodo(self):
        print(self.nome)
        
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo {alimento}.")
            return
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        
        print(f"{self.nome} parou de comer.")
        self.comendo = False