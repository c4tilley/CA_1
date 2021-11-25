"""
# File          : 2.1.py
# Created       : 23/11/2021 14:30
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

#prep BeautifulSoup and pull html data
#print readable text only from data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup.getText())

#use soup to find headers using class in html page and print result
page = soup.find_all("div", {"class":"section_header"})

print(page)
#output shows each heading with class & tag