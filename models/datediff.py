#! /bin/python3

from datetime import datetime
import pandas as pd

air_canada = pd.read_csv("../datasets/participant_data.csv")
ls = list()

# print(type(air_canada))
# print(air_canada["flight_departure_datetime"])
# print(type(air_canada["flight_departure_datetime"]))
# print(air_canada["flight_departure_datetime"].iloc[0])
# print(type(air_canada["flight_departure_datetime"].iloc[0]))

for i in range(len(air_canada)):
    departure = air_canada["flight_departure_datetime"].iloc[i]
    purchase = air_canada["purchase_datetime"].iloc[i]
    dep_obj = datetime.strptime(departure, "%Y-%m-%d %H:%M")
    pur_obj = datetime.strptime(purchase, "%Y-%m-%d %H:%M")
    diff = (dep_obj - pur_obj).total_seconds()
    ls.append(diff)
air_canada.insert(5, "date_difference", ls, True)
print(air_canada["date_difference"])
air_canada.to_csv("../datasets/new_data.csv")
