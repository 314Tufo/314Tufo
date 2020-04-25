# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 9.4 Pyhton Data Structures

Write a program to read through the mbox-short.txt and figure out who has sent the greatest number 
of mail messages. The program looks for 'From ' lines and takes the second word of those lines as 
the person who sent the mail. The program creates a Python dictionary that maps the sender's mail 
address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
fh = open("mbox-short.txt")
counts = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.split()
    counts[line[1]] = counts.get(line[1],0) + 1
bigcount = None
bigword = None
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
print(bigword, bigcount)