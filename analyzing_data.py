# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:31:28 2022

@author: Nevermore
"""

import pandas as pd
import time as t

url = "https://www.statista.com/statistics/1104709/coronavirus-deaths-worldwide-per-million-inhabitants/"
t.sleep(2)
df = pd.read_html(url, match="Characteristic")
df = df[0]
df.rename(columns = {"Characteristic":"Country"}, inplace = True)

def sub_country_name(i:int,country:str):
    """Given the indice 'i' of a country in the dataframe, substitutes its name for the
    'country' argument.
    """
    df.loc[i,["Country"]] = f"{country}"
    return country

sub_country_name(17, "USA")
sub_country_name(26, "UK")
sub_country_name(35, "France")
sub_country_name(53, "Netherlands")
sub_country_name(63, "Denmark")
sub_country_name(100, "UAE")

brazil = df[df["Country"] == "Brazil"]
australia = df[df["Country"] == "Australia"]
usa = df[df["Country"] == "USA"]

description = df.describe()
# print(description)

# Countries with less than 1 million confirmed cases of COVID-19
least_infections = df["Confirmed cases (absolute)"] < 1e6
w = df[least_infections].sort_values("Confirmed cases (absolute)", ascending=False)

# Countries with over 1 thousand deaths per million of total population
most_deaths = df["Deaths per million (total)"] > 1e3
d = df[most_deaths].sort_values("Deaths per million (total)", ascending=False)

# w.plot.bar(x="Country",y="Deaths per million (total)")

# Country with the most deaths per number of cases
mortality = w["Deaths per million (total)"].max()
highest = df["Deaths per million (total)"] == mortality
country = df[highest]
print(country["Country"])

# Country with most total deaths
death = df["Confirmed deaths (absolute)"].max()
absolute = df["Confirmed deaths (absolute)"] == death
c = df[absolute]
print("Country with most total deaths:",c["Country"])

# Total cases
total_cases = df["Confirmed cases (absolute)"]
print("Total worldwide confirmed cases of COVID-19:",sum(total_cases))

# Total deaths
total_deaths = df["Confirmed deaths (absolute)"]
print("Total worldwide confirmed deaths caused by COVID-19:",sum(total_deaths))

# Worldwide deaths per case
dpc = sum(total_deaths)/sum(total_cases)
print("Worldwide deaths per case:",dpc)

def main():
    print("COVID-19 data")

if __name__ == '__main__':
    main()