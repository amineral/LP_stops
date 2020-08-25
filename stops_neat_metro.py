from math import sin, cos, pi, acos
import csv
import json

def dist(lat_a, long_a, lat_b, long_b):
    rad = 6372
    lat_a = float(lat_a) * pi / 180
    lat_b = float(lat_b) * pi / 180
    long_a = float(long_a) * pi / 180
    long_b = float(long_b) * pi / 180

    d = (sin(lat_a) * sin(lat_b)) + (cos(lat_a) * cos(lat_b) * cos(long_a - long_b))
    d = acos(d)
    distance = d * rad

    return distance

def get_stops():  # получает остановки из stop.csv
    stop_list = []
    with open('stops.csv', newline='', encoding='windows-1251') as f:
        reader = csv.DictReader(f, delimiter=';')
        for item in reader:
            stop_list.append(item)
            
    return(stop_list)

def get_metro():  # получает станции метро из metro.json 
    metro = []
    with open("metro.json", "r", encoding='windows-1251') as read_file:
        data = json.load(read_file)
        for item in data:
            metro.append(item)

    return metro
    
def stations_around_metro(metro, stops): #считает количество станций вокруг станции метро. Возвращает список остановок
    count_stops = []
    for stop in stops:
        distance = dist(metro['Latitude_WGS84'], metro['Longitude_WGS84'], stop['Latitude_WGS84'], stop['Longitude_WGS84'])
        if distance <= 0.5:
            count_stops.append(stop['Name'])

    return count_stops

metro_nearest_stops_count = {}
stops = get_stops()
metro_all = get_metro()
#test = []                            # Для тестов
#test.append(metro_all[0])
#test.append(metro_all[10])
#test.append(metro_all[20])

# Проходимся по каждой станции метро и получаем список остановок вокруг станции.
# В словарь metro_nearest_stops_count добавляется ключ с названием станции и значением список остановок вокруг.
# Если такой ключ уже есть, то списки просто объединяются.
for metro in metro_all:
    m = stations_around_metro(metro, stops)
    if metro['NameOfStation'] in metro_nearest_stops_count:
        metro_nearest_stops_count[metro['NameOfStation']] += m
    else:
        metro_nearest_stops_count[metro['NameOfStation']] = m

# В словаре для каждой станции список преобразовуется в сет уникальных значений,
# а затем для каждого ключа запсывается длинна сета(количества уникальных остановок).
for item in metro_nearest_stops_count:
    metro_nearest_stops_count[item] = (len(set(metro_nearest_stops_count[item])))

# Выводится станция с наибольшей длинной сета(количеством-остановок)
max_stops_station = max(metro_nearest_stops_count, key=metro_nearest_stops_count.get)
print(f"{max_stops_station} : {metro_nearest_stops_count[max_stops_station]}")

#ВДНХ - 36
#Юго-Западная - 35

#Возможно немного некорректная формула рассчета расстояний


