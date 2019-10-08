- Change in to the Paramiko directory: ```cd paramiko```

Script: 1_router_connect.py<br>
```python 1_router_connect.py```

- Most basic connection to a router
- This script automates an SSH session in to a router and runs: 'show version'
- Statically assigned variables within the script

Script: 2_router_connect.py<br>
```python 2_router_connect.py XE01_LAB 'show run'```

- Securely read in password from CLI with getpass module
- Added a status message - Retrieving output from:
- Take in router hostname and command variable at CLI

Script: 3_router_connect.py<br>
```python 3_router_connect.py XE01_LAB 'show run'```

- Added writing returned output to a file
- Swapping lines 22 and 23 make for unique file based on router name

Script: 4_router_connect.py<br>
```python 4_router_connect.py 'show run'```

- Added a list of routers to run the for loop against
- Creates a unique file per router

Script: 5_router_connect.py<br>
```python 5_router_connect.py 'show run'```

- Added try/except
- Better error handling

 [NEXT: Go to Netmiko examples](https://github.com/mikesaur/public/tree/master/Python_101/netmiko)
