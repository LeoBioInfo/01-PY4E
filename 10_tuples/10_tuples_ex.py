#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:00:00 2019

@author: leo
"""

"""

10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the 
hour out from the 'From ' line by finding the time and then splitting the 
string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.

Desired Output

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        spline = line.split(':')
        counts[spline[0][-2:]] = counts.get(spline[0][-2:], 0) + 1

t = list(counts.items())
t.sort()
for hour,time in t:
    print (hour, time)
"""
hour = None
times = -1
for hour, tim in counts.items():
    if tim > times:
        times = tim
        procomm = hour
print(procomm, times)
"""

"""
###############################################################################

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
"""
