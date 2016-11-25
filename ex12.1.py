# -*- coding:utf-8 -*-
#!/usr/bin/python 
# filename" ex12.1.py

import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

urlstr = raw_input('Enter the url http://www.py4inf.com/code/romeo.txt - ')
words = urlstr.split('/')
fname = words[-1]
address = re.findall('//(.+?com)/', urlstr)[0]
location = 'GET ' + urlstr + ' HTTP/1.0\n\n'
    
try:
    print location, address
    mysock.connect((address, 80))
    mysock.send(location)
except:
    print 'Please check your url: ' + urlstr
    exit()

try:
    fhand = open(fname, 'wb')
except:
    print 'Open file' + fname + 'failed'
    exit()
        
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    fhand.write(data)

fhand.close()
mysock.close()
