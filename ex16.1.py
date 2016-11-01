# -*- coding:utf-8 -*-
#!/usr/bin/python
# filename: ex16.1.py
# walk through a dir and its sub-dir to check .mp3 files which have the same size

# import
import os
from os.path import join

# define vars
mp3_dict = dict()
start_dir = raw_input('Enter full path of the dir you want to check:')

for (dirname, dirs, files) in os.walk(start_dir):
    for filename in files:
        if filename.endswith('.mp3') :
            thefile = os.path.join(dirname,filename)
            
            try:
                size = os.path.getsize(thefile)
            except:
                continue
            
            if size not in mp3_dict:
                mp3_dict[size] = filename
            else:
                print filename, mp3_dict[size]


 
