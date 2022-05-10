# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:53:30 2022

@author: Nevermore
"""

import pandas as pd

file = pd.read_csv("beyondtime.csv", parse_dates=["Dates"])

# file.plot(x = "Dates", y = "searches")

description = file.describe()
print(description)