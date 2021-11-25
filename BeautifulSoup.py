"""
# File          : BeautifulSoup.py
# Created       : 24/11/2021 11:05
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""

import urllib.request
with urllib.request.urlopen('http://192.168.11.130') as response:
    html = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#print(soup.text.lower())

#for link in soup.find_all('a'):
    #print(link.get('href'))

#print (soup.findAll('b'))