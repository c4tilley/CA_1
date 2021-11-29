"""
# File          : port_scan_test.py
# Created       : 29/11/2021 14:56
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""

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
      for port in range(20, 81):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((remoteServerIP, port))
         if result == 0 and (port == 22):
            print ("Port SSH {}: Open".format(port))
         elif result == 0 and (port == 80):
            print ("Port HTML {}: Open".format(port))
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