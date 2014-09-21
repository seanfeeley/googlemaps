import os, sys
import json, requests
import time
# from googlemaps import GoogleMaps
# "mode=transit"

# gmaps = GoogleMaps("AIzaSyBC_D7ukXVtW0I2LCmqApX479cxvYualKw")
# start = '81 Tierney Road London'
# end   = '15 Margaret Street London'
# dirs  = gmaps.directions(start, end,mode="transit") 
# time  = dirs['Directions']['Duration']['seconds']
# print time/60
# dist  = dirs['Directions']['Distance']['meters']
# route = dirs['Directions']['Routes'][0]
# # for step in route['Steps']:
# #    print step['Point']['coordinates'][1], step['Point']['coordinates'][0] 
# #    print step['descriptionHtml']

home=[51.444848,-0.127986]
work=[51.517005,-0.140360]


def secondsToGetTo(home,dest):
	url="https://maps.googleapis.com/maps/api/directions/json?origin=%f,%f&destination=%f,%f&key=AIzaSyCewGtfayH4MKxjtHpqJjpol8Q2dcKCDW8&&departure_time=%d&mode=transit"
	url= url%(home[0],home[1],dest[0],dest[1],time.time())
	# print url
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	routes=data['routes']
	seconds=data['routes'][0]['legs'][0]['duration']['value']
	return seconds


print secondsToGetTo(home,work)/60
