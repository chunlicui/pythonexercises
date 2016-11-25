# -*- coding:utf-8 -*-
#!/usr/bin/python 
# filename" ex12.3.py

import urllib

url = raw_input('Enter: ')

try:
    fhand = urllib.urlopen(url)
except:
    print 'connected failed, please check your url: ' + url

count = 0

for line in fhand:
    for item in line:
        if item.isalpha():
            count += 1
            if count < 3000:
                print item
                  
fhand.close()
print 'characters count is %d' % (count)

