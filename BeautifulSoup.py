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

#import urllib.request
#with urllib.request.urlopen('http://192.168.11.130') as response:
    #html = response.read()

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html, 'html.parser')

#print(soup.text.lower())

#for link in soup.find_all('a'):
    #print(link.get('href'))

#print (soup.findAll('b'))

import socket
import subprocess
import sys
from datetime import datetime

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = "192.168.11.130"
port = int(input('Please enter port: '))

location = ((address), (port))
result_of_check = a_socket.connect_ex(location)

#if result_of_check == 0 and 80:
   #print("HTML Port 80 is open")
#if result_of_check == 0 and 22:
#print("SSH Port 22 is open")
if result_of_check == 0:
    print("Port is open")
else:
   print("Port is not open")

