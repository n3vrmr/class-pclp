# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:31:18 2022

@author: Nevermore
"""

import pandas as pd

rsf = pd.read_csv("rsf_2022_data.txt")

description = rsf.describe()
print(description)

# Sorting by political score
pol = rsf.sort_values("Score pol.", ascending=False)
print(pol.head())
# Sorting by economical score
eco = rsf.sort_values("Score eco.", ascending=False)
print(eco.head())
# Sorting by legislation score
law = rsf.sort_values("Score leg.", ascending=False)
print(law.head())
# Sorting by social score
soc = rsf.sort_values("Score soc.", ascending=False)
print(soc.head())
# Sorting by score security
sec = rsf.sort_values("Score security", ascending=False)
print(sec.head())

# Countries with a Global Score above 70
highest = rsf[rsf["Global Score"] > 70]

# Largest difference between 2021 and 2022 rank
difference_21 = rsf["Dif. position 2021"].abs().max()
print(difference_21)

d = rsf[rsf["Dif. position 2021"] == -difference_21] # tried with positive value first, which returned an empty dataframe
print("Country with the largest difference in rank compared to 2021:",d["Countries"].values[0])

# Lowest global score
print(rsf[rsf["Global Score"] == rsf["Global Score"].min()])
# Lowest political score
print(pol[pol["Score pol."] == pol["Score pol."].min()])
# Lowest economical score
print(eco[eco["Score eco."] == eco["Score eco."].min()])
# Lowest legislation score
print(law[law["Score leg."] == law["Score leg."].min()])
# Lowest social score
print(soc[soc["Score soc."] == soc["Score soc."].min()])
# Lowest score security
print(sec[sec["Score security"] == sec["Score security"].min()])

def ranking(country):
    """
    Finds the press freedom rank of a country for the year of 2022 and compares
    it to the country's rank in 2021.

    Parameters
    ----------
    country : Name of the country

    Returns
    -------
    rank : Current press freedom rank according to RSF

    """
    current = rsf[rsf["Countries"] == f"{country}"]
    rank = current["Position"].values[0]
    print(f"The current rank of {current['Countries'].values[0]} is {rank}")
    find = rsf[rsf["Countries"] == f"{country}"]
    previous_rank = find["Position"].values[0] + find["Dif. position 2021"].values[0]
    print(f"The previous rank of {find['Countries'].values[0]} was {previous_rank}")
    return rank, previous_rank

ranking("Hong Kong")
ranking("Ireland")
ranking("Argentina")
ranking("Angola")

# Overall, has press freedom increased or decreased from 2021?
info = rsf.sort_values("Dif. position 2021", ascending=False)

"""Looking at the 'info' dataframe, it seems that more countries have larger
differences in their rank to the negative, that is, the difference is greater
on the negative side. However, because this list always has the same 180
countries, adding all the values together will return 0. Therefore, we can
add the values on each side starting from an arbitrary value, such as 29,
for example."""

def difference(x):
    """
    Calculates the total difference in ranks by adding the positive values and adding
    the negative values separately, starting at a difference of ranks defined
    by the argument.

    Parameters
    ----------
    x : Absolute numerical value for the difference in ranks that will be
    calculated.

    Returns
    -------
    total : Total difference between negative and positive rank differences.

    """
    low = sum(i for i in info["Dif. position 2021"] if i < -x)
    high = sum(i for i in info["Dif. position 2021"] if i > x)
    total = low + high
    print(f"Total difference in ranks from 2021 for a difference of {x} ranks or more is {total} ({low} ranks of difference on the negative side, {high} ranks of difference on the positive side.")
    return total

difference(29)
# for x in range(57):
#     difference(x)

"""As the value of x in the 'difference(x)' function increases, you will notice 
that the total difference in ranks is dominated by the negative side (starting
at a difference of 20 ranks, the total is always negative), thus answering the
original question: from 2021 to 2022, press freedom has decreased.
"""

# Brazil
brazil = rsf[rsf["Countries"] == "Brazil"]
print(brazil)

def main():
    print("Press Freedom rankings")
    
if __name__ == '__main__':
    main()