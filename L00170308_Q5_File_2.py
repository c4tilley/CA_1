"""
# File          : L00170308_Q5_File_2.py
# Created       : 26/11/2021 18:36
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
import paramiko
import time

def ssh_connection():
    global user_file
    global cmd_file

    try:
        ip = "192.168.11.130"
        user_name = "l00170308".rstrip("\n")
        user_password = "7113".rstrip("\n")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(ip.rstrip("\n"), username=user_name, password=user_password)
        connection = session.invoke_shell()
        session.exec_command("mkdir This\n")

