#! /bin/python3

from datetime import datetime
import pandas as pd

air_canada = pd.read_csv("../datasets/participant_data.csv")
diff_date = list()
# ratio_price = list()
# origin = list()
# destination = list()
pref_inventory = list()
advs_ratio = list()
pref_ratio = list()
# total = list()
new_pref_price = list()
new_advs_price = list()
time_day = list()

for i in range(len(air_canada)):
    # origin.append(air_canada["od"].iloc[i][0])
    # destination.append(air_canada["od"].iloc[i][3])

    departure = air_canada["flight_departure_datetime"].iloc[i]
    purchase = air_canada["purchase_datetime"].iloc[i]
    dep_obj = datetime.strptime(departure, "%Y-%m-%d %H:%M")
    pur_obj = datetime.strptime(purchase, "%Y-%m-%d %H:%M")
    diff = (dep_obj - pur_obj).total_seconds()
    diff_date.append(diff)

    if dep_obj.hour < 8 or dep_obj.hour > 22:
        time_day.append("night")
    elif dep_obj.hour >= 8 or dep_obj.hour <= 22:
        time_day.append("day")

    # advs_price = int(air_canada["ADVS_price"].iloc[i])
    # pref_price = int(air_canada["PREF_price"].iloc[i])
    # ratio = advs_price / pref_price
    # ratio_price.append(ratio)

    # pref_inventory.append(1 if int(air_canada["PREF_inventory"].iloc[i]) > 0 else 0)
    if (
        int(air_canada["number_of_pax"].iloc[i])
        <= int(air_canada["PREF_inventory"].iloc[i])
        or int(air_canada["PREF_inventory"].iloc[i]) > 0
    ):
        pref_inventory.append(1)
    else:
        pref_inventory.append(0)

    advs_ratio.append(
        int(air_canada["ADVS_inventory"].iloc[i])
        / int(air_canada["ADVS_capacity"].iloc[i])
    )
    pref_ratio.append(
        int(air_canada["PREF_inventory"].iloc[i])
        / int(air_canada["PREF_capacity"].iloc[i])
    )
    # total.append(
    #     int(air_canada["PREF_capacity"].iloc[i])
    #     + int(air_canada["ADVS_capacity"].iloc[i])
    # )

    branded = int(air_canada["branded_fare"].iloc[i])
    if branded == 2:
        new_advs_price.append(0)
        new_pref_price.append(int(air_canada["PREF_price"].iloc[i]))
    elif branded == 3:
        new_pref_price.append(0)
        new_advs_price.append(0)
    else:
        new_pref_price.append(int(air_canada["PREF_price"].iloc[i]))
        new_advs_price.append(int(air_canada["ADVS_price"].iloc[i]))

# air_canada.insert(3, "origin", origin, True)
# air_canada.insert(4, "destination", destination, True)
air_canada.insert(5, "time_diff", diff_date, True)

air_canada = air_canada.drop(columns=["ADVS_price", "PREF_price"])
air_canada.insert(9, "ADVS_price", new_advs_price, True)
air_canada.insert(10, "PREF_price", new_pref_price, True)

# air_canada.insert(13, "PREF_price/ADVS_price", ratio_price, True)
air_canada.insert(15, "pref_inv_full", pref_inventory, True)

air_canada.insert(16, "advs_ratio", advs_ratio, True)
air_canada.insert(17, "pref_ratio", pref_ratio, True)
air_canada.insert(18, "time_day", time_day, True)
print(air_canada.columns)
print(air_canada.head)
air_canada.to_csv("../datasets/new_branded_data.csv")
