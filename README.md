Here are some sample scripts for starting out with Python for Network Engineers<br>
There are so many great modules out there to leverage.

Install Tools

Step 1: Install Windows Subsystem for Linux (WSL)<br>
<i>Note: I suggest Ubuntu</i><br>
- Run Windows PowerShell with elevated priviledges:
    - In the search bar type "powershell"
    - When it pops up right-click on it and choose "Run as administrator"
    - Paste in the command from Step one on the following link: [WSL install instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
    - Follow the rest of the instructions on Microsoft website before moving to next step 

Step 2: Open Ubuntu WSL:
- From the Start button type in: "ubuntu"
- You'll see the Ubuntu 18.04 LTS app show up, click on it
- You should now be in a bash shell prompt (Ubuntu)
- It will ask you to create your user account and password

Step 3: Update Ubuntu:<br>
```sudo apt update && sudo apt upgrade```

Step 4: Install unzip:<br>
 ```sudo apt install unzip```<br>


Step 5: Install python virtual environment:<br>
 ```sudo apt install virtualenv```<br>

Step 6: Setup a virtual environment:<br>
    - ```virtualenv -p python3 venv```<br>
    - ```source venv/bin/activate```<br>

Step 7: Clone repository:<br>
 ```git clone https://github.com/mikesaur/public.git```

Step 8: Install python package manager:<br>
```sudo apt install python3-pip```<br>

Step 9: Move in to the Python_101 directory:<br>
 ```cd public/Python_101```<br> 
 
Step 10: Install python modules:<br>
 ```pip3 install -r requirements.txt```<br>
   
Step 11: Add host entries to /etc/hosts<br>
```sudo cat host_additions.txt | sudo tee -a /etc/hosts```

Step 12: VPN in to CCI Systems Automation Lab<br>

Step 13: Validate you can ping a router in the lab:<br>
```ping XE01_LAB```<br>

Step 14: Create windows shortcut to Linux file system
- Right-click on desktop, add new shortcut
- Path: 
```C:\Users\username\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_*\LocalState\rootfs\home\linuxusername\public```
- at the '*' it doesn't matter whats after the underscore<br>

Step 15: [NEXT: Go to Paramiko examples](https://github.com/mikesaur/public/tree/master/Python_101/paramiko)

 