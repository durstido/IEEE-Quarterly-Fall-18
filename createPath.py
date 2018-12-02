from geoloc import addressToDistance
import numpy as np
import googlemaps
import folium
import math

origin = "9500 Gilman Drive, La Jolla, CA"

def Path(addresses):
    gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

    distances = []
    dis = {}
    distances1 = {}

    for entry in addresses:
        distances.append(entry)
        for i in range(len(addresses)):
            if entry != addresses[i]:
                dis[addresses[i]] = float(addressToDistance(entry, addresses[i]))
                distances1[entry] = dis

    add=[]
    print(distances1)

    #all-nodes shortest path algorithm taken (and modified) from https://stackoverflow.com/questions/38442830/all-nodes-shortest-paths
    for start in addresses:
        nodes = addresses
        distances = distances1
        current = start
        currentDistance = 0
        unvisited = {node: None for node in nodes} 
        visited = {}
        unvisited[current] = currentDistance

        while True:
            for neighbour, distance in distances[current].items():
                if neighbour not in unvisited: continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited: break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

        #our continued code
        if start == origin:
            for i in visited.keys():
                    loc = gmaps.geocode(i)
                    x = ((loc[0]['geometry']['location']['lat']), (loc[0]['geometry']['location']['lng']))
                    add.append(x)
    
    return add

#example:
'''
address4 = "4296 Corte Langostino, San Diego, CA"
address3 = "12871 Pine Meadow Ct, San Diego, CA"
address2 = "4472 Heritage Glen Ln, San Diego, CA"

address5 = "8175 Regents Rd, San Diego, CA"
address6 = "5544 Regents Rd, San Diego, CA"
origin = "9500 Gilman Drive, La Jolla, CA"
address7 = "2966 Massasoit Ave, San Diego, CA"
gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

addresses = [origin, address2, address3, address4]
points = Path(addresses)

lat = []
Long = []

for i in range(len(addresses)):
    loc = gmaps.geocode(addresses[i])
    lat.append(loc[0]['geometry']['location']['lat'])
    Long.append(loc[0]['geometry']['location']['lng'])

mapit = folium.Map(location=[lat[0], Long[0]], zoom_start=12)
for i in range(len(lat)):
    folium.Marker(location=[lat[i], Long[i]]).add_to( mapit )

folium.PolyLine(points).add_to(mapit)

mapit.save('/Users/durstido/Desktop/map.html')
'''

