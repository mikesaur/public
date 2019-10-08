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

Step 4: Install python virtual environment:<br>
 ```sudo apt install virtualenv```<br>

Step 5: Setup a virtual environment:<br>
    - ```virtualenv -p python3 venv```<br>
    - ```source venv/bin/activate```<br>

Step 6: Clone repository:<br>
 ```git clone https://github.com/mikesaur/public.git```

Step 7: Install python package manager:<br>
```sudo apt install python3-pip```<br>

Step 8: Move in to the Python_101 directory:<br>
 ```cd public/Python_101```<br> 
 
Step 9: Install python modules:<br>
 ```pip3 install -r requirements.txt```<br>
   
Step 10: Add host entries to /etc/hosts<br>
```sudo cat hosts_add.txt | sudo tee -a /etc/hosts```

Step 11: VPN in to CCI Systems Automation Lab<br>

Step 12: Validate you can ping a router in the lab:<br>
```ping XE01_LAB```<br>

Step 13: Create windows shortcut to Linux file system
- Right-click on desktop, add new shortcut
- Path: 
```C:\Users\username\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_*\LocalState\rootfs\home\linuxusername\public```
- at the '*' it doesn't matter whats after the underscore<br>

Step 13: Install SublimeText3 - Optional <br>
    - If you do not have a code editor go to: <br>
    ```https://download.sublimetext.com/Sublime%20Text%20Build%203211%20Setup.exe``` 
    
Step 14: [NEXT: Go to Paramiko examples](https://github.com/mikesaur/public/tree/master/Python_101/paramiko)

 