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

# address and user/pass established for SSH connection
hostname = "192.168.11.130"
username = "l00170308"
password = "7113"
# commands for remote ubuntu terminal
commands = ["pwd", "id", "uname -a", 'mkdir -p Labs/{Lab1,Lab2}', 'ls -l --time=atime', 'stat /home']

# command_input = input(f"l00170308@ubuntu:-$:"  )#

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("Unable to connect")
    client.close()


for command in commands:

    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    error = stderr.read().decode()
    if error:
        print(error)

client.close()
