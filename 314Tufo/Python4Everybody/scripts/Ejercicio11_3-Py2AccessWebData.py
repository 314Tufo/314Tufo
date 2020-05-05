# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 11.3 Pyhton to Access Web Data

In this assignment you will read through and parse a file with text and numbers. You will extract 
all the numbers in the file and compute the sum of the numbers.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_461044.txt (There are 85 values and the sum ends with 834)
"""
import re
suma = 0
#sample fh = open("../text_files/regex_sum_42.txt")
fh = open("../text_files/regex_sum_461044.txt")
for line in fh:
    #Crea una lista de numeros en forma de str por cada linea del texto
    numbers = re.findall('[0-9]+',line)
    #Si en una linea del texto no hay numeros, devuelve una lista vacia, con esto la eliminamos
    if len(numbers) == 0:
        continue
    #Esas listas pueden tener mas de un numero si hay mas de un numero por linea del texto.
    #Aqui recorremos esas listas pasando los numeros a enteros y sumandolos al total
    for i in numbers:
        suma += int(i)
print(suma)

