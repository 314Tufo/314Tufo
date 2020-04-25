# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 7.2 Pyhton Data Structures

Write a program that prompts for a file name, then opens that file and reads 
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
suma = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #En realidad lo suyo es eliminar "X-DSPAM-Confidence:" y hacer un lstrip y quedarse con el resto
    x = line.find("0")
    line = line[x:]
    suma = suma + float(line)
    count += 1
print("Average spam confidence:",suma/count)

