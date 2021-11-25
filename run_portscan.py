"""
# File          : run_portscan.py
# Created       : 25/11/2021 13:15
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""

'''Sockets code to carry out a port scan'''
'''Modified from: R.G Lennon Network Examples Part 1 Nov.2021'''

import socket
import subprocess
import sys
from datetime import datetime

def port_scan():
    subprocess.call("cls", shell=True)

    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("-"*60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-"*60)

    t1 = datetime.now()

    try:
        for port in range (79,81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {} : Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()

    total = t2 - t1

    print("Scanning COmpleted in: ", total)

if __name__ == "__main__":
    port_scan()
