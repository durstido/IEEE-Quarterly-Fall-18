import googlemaps
import json


#api key
gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

#get user address
loc_json = gmaps.geocode('100 Walton Street, Crescent City, CA')
user_geoloc = loc_json[0]['geometry']['location']

#get ucsd address
ucsd_address = '9500 Gilman Dr, La Jolla, CA'
ucsd_json = gmaps.geocode(ucsd_address)
ucsd_geoloc = ucsd_json[0]['geometry']['location']

"""
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
