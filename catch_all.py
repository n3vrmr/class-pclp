# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:45:16 2022

@author: Nevermore
"""

from escritor_class import Escritor
from escritor_class import Caneta
from escritor_class import TypeWriter

escritor = Escritor("Edgar Allan Poe")
caneta = Caneta("Pena")
maquina = TypeWriter()

escritor.tool = maquina
escritor.tool.escrever()

from ecommerce import Cart
from ecommerce import Produto

cart = Cart()
p1 = Produto("Guaraná", 12)
p2 = Produto("Sucrilhos", 30)
p3 = Produto("Carne", 110)

cart.inserir_produto(p1)
cart.inserir_produto(p2)
cart.inserir_produto(p3)
cart.inserir_produto(p1)
cart.inserir_produto(p2)

cart.lista_produtos()
print(cart.soma_total())