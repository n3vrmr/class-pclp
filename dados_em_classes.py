# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:59:06 2022

@author: Nevermore
"""
import random

class BaseDados:
    def __init__(self):
        self.dados = {}
        
    def gerar_id(self):    
        y = []
        for i in range(5):
            rand = str(random.randint(0,9))    
            y.append(rand)
        digits = "".join(y)
        return digits
        
    def inserir_cliente(self,nome,id=0):
        id = self.gerar_id()
        if "clientes" not in self.dados:
            self.dados["clientes"] = {nome:id}
        else:
            self.dados["clientes"].update({nome:id})
    
    def lista_clientes(self):
        for nome, id in self.dados["clientes"].items():
            print(nome, id)
    
    def apagar_cliente(self,nome):
        del self.dados["clientes"][nome]
        
bd = BaseDados()
bd.inserir_cliente("Carlos")
bd.inserir_cliente("Rogério")
bd.inserir_cliente("Jéssica")
bd.inserir_cliente("Clara")
bd.inserir_cliente("Ana")
# bd.apagar_cliente("Rogério")