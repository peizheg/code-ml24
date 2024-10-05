#! /bin/python3

from datetime import datetime
import pandas as pd

air_canada = pd.read_csv("../datasets/participant_data.csv")
diff_date = list()
ratio_price = list()
origin = list()
destination = list()
advs_inventory = list()
pref_inventory = list()

for i in range(len(air_canada)):
    od = air_canada["flight_departure_datetime"].iloc[i]
    origin.append(chr(int(air_canada["flight_departure_datetime"].iloc[i][0]) + 64))
    destination.append(
        chr(int(air_canada["flight_departure_datetime"].iloc[i][3]) + 64)
    )

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

    advs_inventory.append(1 if int(air_canada["ADVS_inventory"].iloc[i]) > 0 else 0)
    pref_inventory.append(1 if int(air_canada["PREF_inventory"].iloc[i]) > 0 else 0)

air_canada.insert(3, "origin", origin, True)
air_canada.insert(4, "destination", destination, True)
air_canada.insert(7, "time_diff", diff_date, True)
air_canada.insert(13, "ADVS_price/PREF_price", ratio_price, True)
# air_canada.insert(18, "advs_inv_full", advs_inventory, True)
air_canada.insert(18, "pref_inv_full", pref_inventory, True)
print(air_canada.columns)
air_canada.to_csv("../datasets/new_data.csv")
