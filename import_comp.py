# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:43:40 2022

@author: Nevermore
"""

from composition import Client

client1 = Client("Annabel Lee", 23)
client1.insert_address("Araxá", "MG")
print(client1.name)
client1.lista_addresses()
del client1

client2 = Client("Lenore", 21)
client2.insert_address("Salvador", "BA")
print(client2.name)
client2.lista_addresses()

client3 = Client("Nevermore", 22)
client3.insert_address("Brasília", "DF")
print(client3.name)
client3.lista_addresses()

print("0000000000000000000000000000000000000000000000000000000000000000000000000000000")