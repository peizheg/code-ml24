#! /bin/python3

from datetime import datetime
import pandas as pd

air_canada = pd.read_csv("../datasets/participant_data.csv")
diff_date = list()
ratio_price = list()
origin = list()
destination = list()
pref_inventory = list()
advs_ratio = list()
pref_ratio = list()
total = list()

for i in range(len(air_canada)):
    origin.append(air_canada["od"].iloc[i][0])
    destination.append(air_canada["od"].iloc[i][3])

    departure = air_canada["flight_departure_datetime"].iloc[i]
    purchase = air_canada["purchase_datetime"].iloc[i]
    dep_obj = datetime.strptime(departure, "%Y-%m-%d %H:%M")
    pur_obj = datetime.strptime(purchase, "%Y-%m-%d %H:%M")
    diff = (dep_obj - pur_obj).total_seconds()
    diff_date.append(diff)

    advs_price = int(air_canada["ADVS_price"].iloc[i])
    pref_price = int(air_canada["PREF_price"].iloc[i])
    ratio = advs_price / pref_price
    ratio_price.append(ratio)

    pref_inventory.append(1 if int(air_canada["PREF_inventory"].iloc[i]) > 0 else 0)

    advs_ratio.append(
        int(air_canada["ADVS_inventory"].iloc[i])
        / int(air_canada["ADVS_capacity"].iloc[i])
    )
    pref_ratio.append(
        int(air_canada["PREF_inventory"].iloc[i])
        / int(air_canada["PREF_capacity"].iloc[i])
    )
    total.append(
        int(air_canada["PREF_capacity"].iloc[i])
        + int(air_canada["ADVS_capacity"].iloc[i])
    )

air_canada.insert(3, "origin", origin, True)
air_canada.insert(4, "destination", destination, True)
air_canada.insert(7, "time_diff", diff_date, True)
air_canada.insert(13, "ADVS_price/PREF_price", ratio_price, True)
air_canada.insert(18, "pref_inv_full", pref_inventory, True)

air_canada.insert(19, "advs_ratio", advs_ratio, True)
air_canada.insert(20, "pref_ratio", pref_ratio, True)
air_canada.insert(21, "total_cap", total, True)
print(air_canada.columns)
air_canada.to_csv("../datasets/new_data.csv")
