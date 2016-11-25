# -*- coding:utf-8 -*-
#!/usr/bin/python 
# filename" ex12.2.py

import socket

url = raw_input('Enter: ')
words = url.split('/')
host = words[2]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    print 'conect......'
    mysock.send('GET '+url+' HTTP/1.0\n\n')
    print 'send......'
except:
    print 'connected failed, please check your url: ' + url

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    for item in data:
        if item.isalpha():
            count = count + 1
            if count < 3000:
                print item
              
mysock.close()
print 'characters count is %d' % (count)

