#! /bin/python3

import pandas as pd

air_canada = pd.read_csv("../datasets/new_data.csv")

# branded fare 2 is flex, 3 is comfort
# 2: adv = 0
# 3: adv = 0 pref = 0
