#!/usr/bin/env python3
import paramiko
import time

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect('XE01_LAB', username='cisco', password='cisco', look_for_keys=False)
remote_conn = remote_conn_pre.invoke_shell()  # actual connection establish
time.sleep(1)
remote_conn.send('term length 0\r')
remote_conn.send('show version\r')
time.sleep(1)
temp_output = remote_conn.recv(30000000)
temp_output2 = temp_output.decode("utf-8", errors="ignore")
print(temp_output2)
remote_conn.send('exit\r')
