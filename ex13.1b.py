# -*- coding:utf-8 -*-
#!/usr/bin/python
# filename: ex13.1b.py

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.google.cn/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
    
    try:
        address_component = results[0].findall('address_component') 
        countrycode = address_component[-1].find('short_name').text
    except:
        countrycode = None
    
    print 'countrycode ', countrycode