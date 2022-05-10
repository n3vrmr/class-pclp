# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:22:06 2022

@author: Nevermore
"""
import random
class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def gan(self):
        print(self.ano_atual - self.idade)
        
    @classmethod
    def pan(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gerar_id():    
        y = []
        for i in range(5):
            rand = str(random.randint(0,9))    
            y.append(rand)
        digits = "".join(y)
        return digits
        
p1 = Pessoa.pan("Nevermore", 1834)
print(f"{p1.nome} tem {p1.idade} anos de idade")

print(f"O número de identidade de {p1.nome} é {Pessoa.gerar_id()}")