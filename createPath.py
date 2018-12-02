from geoloc import addressToDistance
import googlemaps

origin = "9500 Gilman Drive, La Jolla, CA"

def Path(addresses): #given a list of string addresses
    gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

    distances = []
    dis = {}
    distances1 = {}

    #create a dictionary where each key is an address, and each value is another dictionary
    #each nested dictionary will have all the other addresses (not the one with the original key), and the values will be their distance to the original key/address
    #for example, for nodes = ('A', 'B', 'C'), the dictionary distances1 will be
    #{ 'A': {'B': 3, 'C': 4}
    #  'B': {'A': 3, 'C': 8}
    #  'C': {'A': 4, 'B': 8}
    
    for entry in addresses:
        distances.append(entry)
        for i in range(len(addresses)):
            if entry != addresses[i]:
                dis[addresses[i]] = float(addressToDistance(entry, addresses[i]))
                distances1[entry] = dis

    add=[]

    #all-nodes shortest path algorithm taken (and modified) from https://stackoverflow.com/questions/38442830/all-nodes-shortest-paths
    #essentially, it will start with the inital value/base (in our example, UCSD), and will check through distances1 the distances to all other points
        #it will then choose the point with the least distance and move to it
        #it will repeat this process with this point, finding the next nearest point (excluding the previous points of course), and so on
        #or at least, this is what we understood of it :)
    
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

        #our own code from here on
        if start == origin: #start at base/origin (UCSD)
            for i in visited.keys(): #all addresses in the order of shortest path 
                    loc = gmaps.geocode(i)
                    x = ((loc[0]['geometry']['location']['lat']), (loc[0]['geometry']['location']['lng'])) #lat and long of each point
                    add.append(x)
    return add
