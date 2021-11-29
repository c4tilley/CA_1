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
###
#import socket
#a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#address = ("192.168.11.130", 80)
#if a_socket.connect_ex(address) == 0:
   #print("Port is open")
#else:
   #print("Port is not open")
# socket.getaddrinfo("192.168.11.130", 22)
# print(socket.getaddrinfo("192.168.11.130", 22))
###

# import and access modules
import socket
import subprocess
import sys
from datetime import datetime

# define port scan and user input for IP address
def port_scan():
   subprocess.call("cls", shell=True)

   remoteServer = input("Enter a remote host to scan:")
   remoteServerIP = socket.gethostbyname(remoteServer)

   print("-" * 60)
   print("Please wait, scanning remote host", remoteServerIP)
   print("-" * 60)

   t1 = datetime.now()
# test ports from range(value,value). Two arguments made with same 0 open requirement.
# both arguments have different variable - if its related to port 22 - display SSH, if its port 80 - display HTML.
   try:
      for port in range(19, 81):
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((remoteServerIP, port))
         if result == 0 and (port == 22):
            print ("Port SSH {}: Open".format(port))
         if result == 0 and (port == 80):
            print ("Port HTML {}: Open".format(port))
         elif result == [0]:
            print ("Port {}: Open".format(port))
# keyboard interrupt if process stalls
   except KeyboardInterrupt:
      print ("you pressed Ctrl+C")
      sys.exit()
# if no response from host error
   except socket.gaierror:
      print ("Hostname could not be resolved. Exiting")
      sys.exit()
# if no response from scoket error
   except socket.error:
      print("Couldn't connect to server")
      sys.exit()
# define current time after process finished and subctract intial time to calcualte totoal and display.
   t2 = datetime.now()
   total = t2 - t1

   print ("Scanning Completed in: ",total)

if __name__=="__main__":
   port_scan()



   #socket.getaddrinfo("192.168.11.130", 22)
   #print(socket.getaddrinfo("192.168.11.130", 22))


