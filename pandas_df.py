#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:21:07 2022

@author: Nevermore
"""

import pandas as pd

poke_excel = pd.read_excel("pokemon_data.xlsx")

# print(poke_excel.columns)
print(poke_excel["Name"][531:553])
print(poke_excel[["Name","#"]][531:553])
# print(poke_excel.head())
description = poke_excel.describe()
print(description)
print(poke_excel["#"].max())
iterator = 0
for name in poke_excel["Name"]:
    if "c" in name:
        iterator = iterator +1
print(poke_excel.loc[0,"Name"])
print(poke_excel.iloc[0,0])

pokemon = "Charizard"
# print(poke_excel["Name"] == pokemon)
# print(poke_excel[poke_excel["Name"] == pokemon])
charizard = poke_excel[poke_excel["Name"] == pokemon]

pokemon_2 = "Typhlosion"
typhlosion = poke_excel[poke_excel["Name"] == pokemon_2]

# poke_excel.plot()
hp = poke_excel["HP"]
# hp.plot()

print(poke_excel["HP"].max())
# poke_excel["HP"] == poke_excel["HP"].max()
print(poke_excel[poke_excel["HP"] == poke_excel["HP"].max()])

print(poke_excel["Type 1"].mode())

tipo1 = poke_excel.groupby("Type 1").count()
print(tipo1)

poke = poke_excel[poke_excel["Attack"] > 100].sort_values("Attack",ascending=False)
print(poke)

duplicados = poke_excel[poke_excel["#"].duplicated()]
print(duplicados["#"].count())
print(duplicados["Name"])

twice = duplicados[duplicados["#"].duplicated()]
print(twice.count())