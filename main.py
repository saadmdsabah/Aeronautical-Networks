import csv
import math
L_M = input("Linear or Multiple\n")

data = []
with open('NA_11_Jun_29_2018_UTC11.CSV','r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        data.append(row)

def convert_to_cartesian(lat,lon,alt):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    x = (float(alt) + 6371000) * math.cos(lat_rad) * math.cos(lon_rad)
    y = (float(alt) + 6371000) * math.cos(lat_rad) * math.sin(lon_rad)
    z = (float(alt) + 6371000) * math.sin(lat_rad)
    return x, y, z

def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance

graph1 = {}
graph2 = {}
ground_stations = {
    'LHR': convert_to_cartesian(51.4700, -0.4543, 81.73),
    'EWR': convert_to_cartesian(40.6895, -74.1745, 8.72)
}

for Flight,Timestamp, Altitude, Latitude, Longitude in data:
    current_node = (Flight,convert_to_cartesian(float(Latitude),float(Longitude),float(Altitude)))
    graph1[current_node] = []
    graph2[current_node] = []
    for gs, gs_coordinates in ground_stations.items():
        distance = calculate_distance(current_node[1], gs_coordinates)
        transmission_rate = 52.875 if distance <= 400 else abs((1000 - distance/100)/1000)
        graph1[current_node].append((gs, transmission_rate))
        
        if(L_M == "multiple"):
            propogation_delay = distance/300000000
    #         peak download spped of between 40 and 100Mbps
            transmission_delay = 70/transmission_rate
    #         latency = transmission delay + propogation delay
            latency = (transmission_delay + propogation_delay)
            graph2[current_node] = latency

routing_paths = []
for node in graph1:
    current_path = [node]
    current_rate = 0
    while current_path[-1][0] not in ground_stations:
        neighbors = graph1[current_path[-1]]
        max_rate = max(neighbors,key=lambda x: x[1])
        current_path.append(max_rate)
        current_rate = max_rate[1]
    routing_paths.append((node[0], current_path, current_rate))
routing_paths.sort(key=lambda x:x[2], reverse = True)

d = False
for Flight,path,rate in routing_paths:
    print(f"Flight No: {Flight}")
    print("Routing Path: ")
    for node in path:
        if(d):
            print(f"- {node[0]}")
            d = False
        else:
            d = True 
    print(f"Maximum Data Transmission Rate: {rate} Mbps")
    if(L_M == "multiple"):
        for lat in graph2:
            print(f"Minimum Latency : {graph2[lat]} seconds")
            del graph2[lat]
            break
    print()

