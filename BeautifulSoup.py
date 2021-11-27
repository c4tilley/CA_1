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

import paramiko

hostname = "192.168.11.130"
username = "l00170308"
password = "7113"

commands = ["pwd","id","uname -a", 'mkdir -p Labs/{Lab1,Lab2}', 'ls -l --time=atime', 'stat /home']

#command_input = input(f"l00170308@ubuntu:-$:"  )#

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print ("Unable to connect")
    client.close()


for command in commands:

    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    error = stderr.read().decode()
    if error:
        print(error)

client.close()