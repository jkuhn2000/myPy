# The program will prompt for a location
# Contact a web service
# Retrieve JSON for the web service
# Parse that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# Data URL:
# 'http://python-data.dr-chuck.net/geojson?sensor=false&address=South+Federal+University'

import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)

    print 'Place ID: ', js["results"][0]["place_id"]

