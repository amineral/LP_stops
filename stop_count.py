import csv

# Вывести улицу, на которой больше всего остановок

def collect_stops():
     with open('stops.csv', newline='', encoding='windows-1251') as f:
        stop_dict = {}
        reader = csv.DictReader(f, delimiter=';')
        for item in reader:
            if item['Street'] in stop_dict:
                stop_dict[item['Street']] += 1
            else:
                if item['Street'] == "проезд без названия":
                    pass
                else:
                    stop_dict[item['Street']]  = 1
        return stop_dict

stops = collect_stops()
max_stops_street = max(stops, key=stops.get)
#max_stops_street = [k for k,v in stops.items() if v==max(stops.values())][0]
print(f"{max_stops_street} : {stops[max_stops_street]}")
