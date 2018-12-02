import googlemaps
import json
import math




#api key
gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

def addressToDistance(address1, address2):
    '''
    Takes 2 addresses and returns the distance between them.
    *** Note the addresses must be passed in as strings ***
    '''
    loc1 = gmaps.geocode(address1)
    lat1 = loc1[0]['geometry']['location']['lat']
    lon1 = loc1[0]['geometry']['location']['lat']

    loc2 = gmaps.geocode(address2)
    lat2 = loc2[0]['geometry']['location']['lat']
    lon2 = loc2[0]['geometry']['location']['lat']

    #print(loc1_lat)
    #print(loc2_lat)

    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers

    meters = round(meters, 3)
    km = round(km, 3)

    #print(f"Distance: {meters} m")
    #print(f"Distance: {km} km")

    return km


address1 = '100 Walton Street, Crescent City, CA'
address2 = '9500 Gilman Dr, La Jolla, CA'

addressToDistance(address1, address2)

#print(addressToDistance(address1, address2))

"""
#get user address
loc_json = gmaps.geocode('100 Walton Street, Crescent City, CA')
user_geoloc = loc_json[0]['geometry']['location']

#get ucsd address
ucsd_address = '9500 Gilman Dr, La Jolla, CA'
ucsd_json = gmaps.geocode(ucsd_address)
ucsd_geoloc = ucsd_json[0]['geometry']['location']


Prints the lat and lng of ucsd and input loc
ucsd_lat = ucsd_geoloc['lat']
ucsd_lng = ucsd_geoloc['lng']

user_lat = user_geoloc['lat']
user_lng = user_geoloc['lng']

print("user lat: ", user_lat)
print("user lng: ", user_lng)

print("warren lat: ", ucsd_lat)
print("warren lng: ", ucsd_lng)
"""
