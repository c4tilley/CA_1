"""
# File          : L00170308_Q4_File_2.py
# Created       : 26/11/2021 15:46
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""

#import socket
#a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#address = ("192.168.11.130", 80)
#if a_socket.connect_ex(address) == 0:
   #print("Port is open")
#else:
   #print("Port is not open")

import socket
import subprocess
import sys
from datetime import datetime

def port_scan():
   subprocess.call("cls", shell=True)

   remoteServer = input("Enter a remote host to scan:")
   remoteServerIP = socket.gethostbyname(remoteServer)

   print("-" * 60)
   print("Please wait, scanning remote host", remoteServerIP)
   print("-" * 60)

   t1 = datetime.now()

   try:
      for port in range(1, 1025):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((remoteServerIP, port))
         if result == 0:
            print ("Port {}: Open".format(port))
         sock.close()
   except KeyboardInterrupt:
      print ("you pressed Ctrl+C")
      sys.exit()

   except socket.gaierror:
      print ("Hostname could not be resolved. Exiting")
      sys.exit()

   except socket.error:
      print("Couldn't connect to server")
      sys.exit()

   t2 = datetime.now()

   total = t2 - t1

   print ("Scanning Completed in: ",total)

if __name__=="__main__":
   port_scan()

