#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:58:53 2019

@author: leo
"""
"""
counts = dict()
names = ['leo', 'belen', 'isa', 'belen', 'leo', 'leo']
for name in names:
    counts[name] = counts.get(name, 0) + 1
    print(counts)
"""
"""
9.4 Write a program to read through the mbox-short.txt and figure out who has 
sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer.

cwen@iupui.edu 5

"""
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        spline = line.split()
        counts[spline[1]] = counts.get(spline[1], 0) + 1
procomm = None
times = -1
for pro, tim in counts.items():
    if tim > times:
        times = tim
        procomm = pro
print(procomm, times)