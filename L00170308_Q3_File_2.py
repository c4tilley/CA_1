"""
# File          : L00170308_Q3_File_2.py
# Created       : 25/11/2021 14:18
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
# import modules for use
import paramiko
import time
import re


# info for SSH connection to VM
def ssh_connection(ip):

    try:
        username = "l00170308"
        password = "7113"
# feedback if successfully connect or error occurs
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        time.sleep(1)
        vm_output = connection.recv(65535)
        if re.search(b"%Invalid input", vm_output):
            print("There was an error on vm{}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection("192.168.11.130")
