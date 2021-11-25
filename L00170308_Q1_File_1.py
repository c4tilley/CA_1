"""
# File          : L00170308_Q1_File_1.py
# Created       : 25/11/2021 14:18
# Author        : C. Tilley
# Version       : V1.0
# Licensing     : (C) 2021 Chris Tilley, LYIT
#
# Description   : DCM_2021_LYIT
#
"""
import paramiko
import time
import re

def ssh_connection(ip):
    try:
        username = "l00170308"
        password = "7113"

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt \n")
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"%Invalid input", vm_output):
            print("There was an error on vm{}".format(ip))
        else:
            print("Commands successfully executed on{}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

ssh_connection("192.168.11.130")

host = "192.168.11.130"
port = 22
username = "l00170308"
password = "7113"

command = "ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

#stdin, stdout, stderr = ssh.exec_command(command)
#lines = stdout.readlines()
#print(lines)

#ssh.connect(host=host, port=port, username=username, password=password)
#paramiko.AutoAddPolicy(set_missing_host_key_policy)
#

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)