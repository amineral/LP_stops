import json
import math

# Вывести все станции, где происходит ремонт эскалатора

repair = {}

with open("metro.json", "r", encoding='windows-1251') as read_file:
    data = json.load(read_file)
    for station in data:
        if station['RepairOfEscalators']:
            repair[station['NameOfStation']] = 1
    for k, v in repair.items() : print(k)

lat_a = 55.42937078 * math.pi / 180
lat_b = 55.74976112 * math.pi / 180

long_a = 36.84124614 * math.pi / 180
long_b = 37.57271647 * math.pi / 180

rad = 6372
d = (math.sin(lat_a) * math.sin(lat_b)) + (math.cos(lat_a) * math.cos(lat_b) * math.cos(long_a - long_b))
d = math.acos(d)
l = d * rad
print(l)
