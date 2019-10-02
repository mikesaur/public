#!/usr/bin/env python3
import sys
import time
import paramiko
import getpass

# Sample Run
### python 3_router_connect.py router1 'show cdp neighbor'

router = sys.argv[1]  # Ask user at CLI what router they want to run command on
command = sys.argv[2]  # Ask user what command they want to run

uname = input('Admin Username: ')
if uname is '':  # allows us to be lazy and just hit enter
    uname = 'cisco'

password = getpass.getpass('Admin Password: ')
if password is '':
    password = 'cisco'

print('Retrieving output from: ' + router)

logfile = open('router_log.txt', 'w')  # Open a file for writing data to
# logfile = open(router + '_config.txt', 'w')

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(router, username=uname, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
time.sleep(1)  # Need to wait for connection to establish
remote_conn.send('term length 0\r')
remote_conn.send(command + '\r')
time.sleep(1)
temp_output = remote_conn.recv(30000000)  # Establish buffer in Ram to receive output from router
temp_output2 = temp_output.decode("utf-8", errors="ignore")
logfile.write(temp_output2)  # Take the contents of the buffer and write a copy to the file
print(temp_output2)  # Display the returned content from the router
remote_conn.send('exit\r')  # Disco from the router
logfile.close()  # Close the file
