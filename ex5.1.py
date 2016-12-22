# -*- coding:utf-8 -*-
#!/usr/bin/python
# filename: ex5.1.py
# enter several numbers and print out the sum, count and average values

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

print "Sum:%f, Count:%f, Average: %f" % (sum(lst), len(lst), sum(lst) / len(lst))

 