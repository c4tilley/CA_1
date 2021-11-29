"""
# File          : L00170308_Q2_File_2.py
# Created       : 23/11/2021 14:30
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
###
#import urllib.request
#with urllib.request.urlopen('http://192.168.11.130') as response:
    #html = response.read()
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html, 'html.parser')
#print(soup.text.lower())
#for link in soup.find_all('a'):
    #print(link.get('href'))
#print (soup.findAll('b'))
###

#prep urlib module.
#urlirb.request used to fetch specific URL, confirm successful response (no errors).
import urllib.request
with urllib.request.urlopen('http://192.168.11.130') as response:
    html = response.read()

#prep BeautifulSoup and pull html data
#print readable text only from data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#display page into more understandbale format
print(soup.getText())

#use soup to find headers using class in html page and print result
page = soup.find_all("div", {"class":"section_header"})

#summary of headers listed with tag/class info
print(page)

#import page look for text without a tag that included 'apache2'
import re
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(text=re.compile("apache2")))