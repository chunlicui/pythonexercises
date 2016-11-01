# -*- coding:utf-8 -*-
#!/usr/bin/python
# filename: ex16.2.py
# walk through a dir and its sub-dir to check .jpg files which have the MD5 value

# import
import os
from os.path import join
import hashlib

# define vars
jpg_dict = dict()
start_dir = raw_input('Enter full path of the dir you want to check:')

for (dirname, dirs, files) in os.walk(start_dir):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.JPG'):
            thefile = os.path.join(dirname,filename)
            
            try:
                fhand = open(thefile, 'r')
                data = fhand.read()
                fhand.close()
                checksum = hashlib.md5(data).hexdigest()                             
            except:
                continue
            
            if checksum not in jpg_dict:
                jpg_dict[checksum] = filename
            else:
                print filename, jpg_dict[checksum]
                
          


 
