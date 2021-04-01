#!/usr/bin/env python

urban_cities = {}

city_count = 0
with open ("Resources/city_data.csv", 'r') as city_data:
    for line in city_data:
        nn = len(line)
        line = line[0:nn-1]
        fields = line.split(",")
        name = fields[0]
        category = fields[2]
        if category == "Urban":
            urban_cities[name] = category

ride_count = 0
with open ("Resources/ride_data.csv", 'r') as ride_data:
    for line in ride_data:
        nn = len(line)
        line = line[0:nn-1]
        fields = line.split(",")
        name = fields[0]
        if name in urban_cities:
            print(name)


