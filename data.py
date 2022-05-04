# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:17:18 2022

@author: Nevermore
"""

import pandas as pd

pokedex_csv = pd.read_csv("pokemon_data.csv")
pokedex_txt = pd.read_csv("pokemon_data.txt",sep='\t')
pokedex_xlsx = pd.read_excel("pokemon_data.xlsx")

col = pokedex_xlsx.columns

print(pokedex_xlsx["Name"])
for name in pokedex_xlsx["Name"]:
    print(name)

# Use functions .loc and .iloc to change values in your dataframe, they create a different 'view' of the dataframe instead of a 'copy'
print(pokedex_xlsx.loc[20:31,["Name","Type 1","HP"]])
print(pokedex_xlsx.iloc[5:16,0:5])

higher = pokedex_xlsx["Attack"] > 119
pokemon_119 = pokedex_xlsx[higher].sort_values("Attack",ascending=False)

hp_higher = pokedex_xlsx["HP"] > 150
pokemon_hp = pokedex_xlsx[hp_higher].sort_values("HP",ascending=True)

description = pokedex_xlsx.describe()
print(description)

selection = pokedex_xlsx["Attack"]
selection.plot(legend=True,xlabel="Pokemon Number",ylabel="Attack")

grouping = pokedex_xlsx.groupby("Type 1").mean()

# missing values

missing = pokedex_xlsx.isna()

missing = pokedex_xlsx[missing["Type 2"]]

# webscrapping

url = "https://pt.wikipedia.org/wiki/COVID-19"
html = pd.read_html(url,match="Frequência")