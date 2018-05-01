#Reverse Geocoding example - gpstracker_revgeo.py - Stavros Kalapothas

import numpy as np
import gmplot
import webbrowser
import googlemaps

latlon=np.loadtxt(r'./stops_part.txt',dtype=str,delimiter=',',skiprows=1,usecols=(4,5)) # parse csv specific columns
#print(latlon) # debug

gmaps = googlemaps.Client(key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') # Google Maps API Key
gmap = gmplot.GoogleMapPlotter(37.983810, 22.727539, 15)    # Athens map object

for x,y in latlon:  # iterate in list
    #print(float(x), float(y))  # debug
    marker = gmap.marker(float(x), float(y), 'cornflowerblue') # add marker for ever lat,lon set
    reverse_geocode_result = gmaps.reverse_geocode((float(x), float(y)),result_type='street_address')
    for address in reverse_geocode_result:  # iterate on json
        print(address['formatted_address'])   # return value from key
    
gmap.draw('./map.html') # draw map

file = "file:///map.html"
tab = 2 # open in a new tab, if possible
webbrowser.open(file,new=tab)   # open file in browser