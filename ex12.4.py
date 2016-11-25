# -*- coding:utf-8 -*-
#!/usr/bin/python 
# filename" ex12.4.py
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib

from lib.BeautifulSoup import *
#from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
count = 0
tags = soup('p')
for tag in tags:
    count += 1

print count

