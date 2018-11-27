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
    loc1_lat = loc1[0]['geometry']['location']['lat']
    loc1_long = loc1[0]['geometry']['location']['lat']

    loc2 = gmaps.geocode(address2)
    loc2_lat = loc2[0]['geometry']['location']['lat']
    loc2_long = loc2[0]['geometry']['location']['lat']

    #print(loc1_lat)
    #print(loc2_lat)

    deltaLat = loc2_lat - loc1_lat
    deltaLong = loc2_long - loc1_long

    return math.sqrt(math.pow(deltaLat, 2) + math.pow(deltaLong, 2))


address1 = '100 Walton Street, Crescent City, CA'
address2 = '9500 Gilman Dr, La Jolla, CA'

print(addressToDistance(address1, address2))

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
