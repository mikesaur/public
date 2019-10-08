Here are some sample scripts for starting out with Python for Network Engineers<br>
There are so many great modules out there to leverage.

Install Tools

Step 1: Install Windows Subsystem for Linux (WSL)<br>
<i>Note: I suggest Ubuntu</i><br>

- Instructions: 
 [WSL install instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Step 1: Open Ubuntu WSL:
- From the Start button type in: "ubuntu"
- You'll see the Ubuntu 18.04 LTS app show up, click on it
- You should now be in a bash shell prompt (Ubuntu)

Step 2: Update Ubuntu:<br>
```sudo apt update && sudo apt upgrade```

Step 2: Install unzip:<br>
 ```sudo apt install unzip```<br>


Step 3: Install python virtual environment:<br>
 ```sudo apt install virtualenv```<br>

Step 4: Setup a virtual environment:<br>
    - ```virtualenv -p python3 venv```<br>
    - ```source venv/bin/activate```<br>

Step 5: Clone repository:<br>
 ```git clone https://github.com/mikesaur/public.git```

Step 6: Install python modules:<br>
 ```pip3 install -r requirements.txt```<br>
   
Step 7: Add host entries to /etc/hosts<br>
```sudo cat host_additions.txt | sudo tee -a /etc/hosts```

Step 8: Move in to the Python_101 directory:<br>
 ```cd public/Python_101```<br> 
 
Step 9: VPN in to CCI Systems Automation Lab<br>

Step 10: Validate you can ping a router in the lab:<br>
```ping XE01_LAB```<br>

 Step 10: [NEXT: Go to Paramiko examples](https://github.com/mikesaur/public/tree/master/Python_101/paramiko)

 