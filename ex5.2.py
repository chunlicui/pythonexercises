# -*- coding:utf-8 -*-
#!/usr/bin/python
# filename: ex5.2.py
# enter several numbers and print out the sum, count, max and min values

lst = list()

while True:
    inp = raw_input("Enter a number: ")
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    lst.append(num)

print "Sum:%f, Count:%f, Max: %f, Min: %f" % (sum(lst), len(lst), max(lst), min(lst))

 