"""
# File          : soup_test.py
# Created       : 24/11/2021 14:48
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
#prep urlib module.
#urlirb.request used to fetch specific URL, confirm successful response (no errors).
import urllib.request
with urllib.request.urlopen('http://192.168.11.130') as response:
    html = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup.text.lower())

for link in soup.find_all('a'):
    print(link.get('href'))

#print (soup.findAll('b'))

import re

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(text=re.compile("apache")))

from bs4 import BeautifulSoup
import requests


