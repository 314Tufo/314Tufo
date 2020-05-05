# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 7.1 Pyhton Data Structures

Write a program that prompts for a file name, then opens that file and reads 
through the file, and print the contents of the file in upper case. Use the 
file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""
# Use words.txt as the file name
fname = input("Enter file name: ")
#Abre el archivo
fh = open(fname)
#Lee línea a línea el archivo
for linea in fh:
    #Elimina el doble espaciado a causa del print
    linea = linea.rstrip()
    #Lo pedría en mayus
    linea = linea.upper()
    print(linea)
