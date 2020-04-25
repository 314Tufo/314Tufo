# -*- coding: utf-8 -*-
"""
Sergio Di Deco Sampedro

Ejercicio 12.6 Pyhton to Access Web Data

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program 
similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from 
the data files below, and parse the data, extracting numbers and compute the sum of the numbers in 
the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your 
testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_461046.html (Sum ends with 70)
You do not need to save these files to your folder since your program will read the data directly 
from the URL. Note: Each student will have a distinct data url for the assignment - so only use your 
own data url for analysis.
"""
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen("http://py4e-data.dr-chuck.net/comments_461046.html", context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#A continuacion imprimimos la web en html
print(soup)

#Devuelve los tags span
tags = soup('span')

#Imprime info de los tags y ademas queremos contabilizar los contents
contents = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    contents += int(tag.contents[0])
    print('Attrs:', tag.attrs)

print(contents)
