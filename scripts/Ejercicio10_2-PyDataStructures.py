# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 10.2 Pyhton Data Structures

Write a program to read through the mbox-short.txt and figure out the distribution by hour of the 
day for each of the messages. You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown 
below.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
fh = open("mbox-short.txt")
counts = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.split()
    hour = line[5]
    hour = hour.split(":")
    counts[hour[0]] = counts.get(hour[0],0) + 1
lista = sorted(counts.items())
for k,v in lista:
    print(k,v)
