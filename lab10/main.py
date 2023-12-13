# ******************************************************************************
# Author:           Jay Abegglen
# Lab:              10
# Date:             11/08/2023
# Description:      Program reads in information from anime.csv, then displays most popular tv shows
#                   in anime based on members versus rating
# Input:            Reads in values from anime.csv
# Output:           plots a bar graph
# Sources:          Lab 10 specifications
# url:              https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database
#
# ******************************************************************************

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

pd.set_option('display.max_columns', 10)

df = pd.read_csv("anime.csv")
print(df)
print(df[["name", "members"]].sort_values("members", ascending=False))
unique_set = df[["name", "rating", "members"]].groupby("name").sum()

# This particular list doesn't appear to have duplicates but I've added the logic as a "just in case"
popular_shows = unique_set.sort_values("members", ascending=False)[:20].reset_index()[::-1]

print(popular_shows)

# plot horizontal bar graph
plt.figure(figsize=(12, 8), dpi=72)
plt.barh(popular_shows["name"], popular_shows["members"])
plt.xlabel("Popularity")
plt.title("Top 20 Most Popular Anime Fan Bases")
plt.ylabel("Anime Names")

# set x-axis notation beforehand
plt.ticklabel_format(style='plain', axis='x')
plt.xlim((500000, 1050000))
pl.tight_layout()
plt.show()
