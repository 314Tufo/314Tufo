# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 13.5 Pyhton to Access Web Data

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that 
URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of 
the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your 
testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_461048.xml (Sum ends with 93)
You do not need to save these files to your folder since your program will read the data directly 
from the URL. Note: Each student will have a distinct data url for the assignment - so only use your 
own data url for analysis.
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_461048.xml'
    
#Esto era del codigo geoxml.py (verlo, es interesante)
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Hago el request de la pagina
uh = urllib.request.urlopen(serviceurl, context=ctx)

counts = list()
suma = 0

data = uh.read()
#Este es mi arbol
tree = ET.fromstring(data)
#Encuentro todos los tags de comment
lista = tree.findall('.//comment')
#Dentro de los tags de comment añado las cuentas a la lista counts y los voy sumando
for item in lista:
    counts.append(item.find('count').text)
    suma += int(item.find('count').text)
print(counts)
print(suma)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    