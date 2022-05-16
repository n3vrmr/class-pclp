# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:52:00 2022

@author: Nevermore
"""

import pandas as pd

pokedex = pd.read_csv("pokemon_data.csv")

# a) Construa uma lista com o nome dos seguintes Pokemons: 'Gastly', 'Trevenant', 'Pikachu' (0,5 ponto).
pokemons = []
def capture_pkmn(pkmn):
    pkmn = pokedex[pokedex["Name"] == f"{pkmn}"]
    pokemons.append(pkmn)
    return pokemons

capture_pkmn("Gastly")
capture_pkmn("Trevenant")
capture_pkmn("Pikachu")
print(pokemons)

# Ou você pode fazer desse jeito:
# gastly = pokedex[pokedex["Name"] == "Gastly"]
# trevenant = pokedex[pokedex["Name"] == "Trevenant"]
# pikachu = pokedex[pokedex["Name"] == "Pikachu"]
# pokemons.append(gastly)
# pokemons.append(trevenant)
# pokemons.append(pikachu)
# print(pokemons)

# b) Altere o último elemento da lista para 'Spiritomb' (0,5 ponto).
spiritomb = pokedex[pokedex["Name"] == "Spiritomb"] 
pokemons[2] = spiritomb
print(pokemons)

# c) Crie um dicionário chamado treinador com as chaves "nome" e "pokemons" cujos valores serão "Ash" e a lista de pokemons criada anteriormente (0,5 ponto).
treinador = {"nome":"Ash","pokemons":pokemons}
print(treinador["nome"])
print(treinador["pokemons"])

# d) Uma nova versão da PokeDex está sendo desenvolvida em Python e o seguinte bloco de código foi escrito para a funcionalidade de buscar um Pokemon pelo nome.
def buscar(nome:str):
    pokemon = pokedex[pokedex["Name"] == nome]
    texto = f"O {pokemon['Name'].values[0]} é do tipo {pokemon['Type 1'].values[0]} e é da geração {pokemon['Generation'].values[0]}."
    print(texto)
    return pokemon

buscar("Gastly")
buscar("Trevenant")
buscar("Spiritomb")

def main():
    print("Cynthia boss music starts playing")

if __name__ == '__main__':
    main()