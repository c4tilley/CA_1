"""
# File          : 2.3.py
# Created       : 25/11/2021 12:45
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
import urllib.request
import re

def read_IP_Addr():
    print ("Find external IP Address")

    #service to display from exnternal IP address
    #url = "https://whatismyipaddress.com" #forbidden
    url = "http://checkip.dyndns.org"
    print(url)
    request2 = urllib.request.urlopen(url)
    request = request2.read()
    print(request)

    request = str(request)
    theIP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',request)

    print("your IP Address is: ", theIP)

if __name__=="__main__":
    read_IP_Addr()


