Here are some sample scripts for starting out with Python for Network Engineers<br>
There are so many great modules out there to leverage.

Install Tools

Step 1: Install Windows Subsystem for Linux (WSL)<br>
<i>Note: I suggest Ubuntu</i><br>

- Instructions: 
 [WSL install instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- Make sure to do the update/upgrade steps on the "activate your WSL install"<br>

Step 2: Install unzip: ```sudo apt install unzip```

Step 3: Install python package manger: ```sudo apt install python3-pip```<br>

Step 3: Install python virtual environment: ```sudo pip3 install virtualenv```<br>

Step 4: Setup a virtual environment:<br>
    -  ```virtualenv -p python3 venv```<br>
    - ```source venv/bin/activate```

Step 5: Clone repository: ```git clone https://github.com/mikesaur/public.git```

Step 6: Move in to the Python_101 directory: ```cd public/Python_101```
   
Step 7: Add host entries to /etc/hosts<br>
 
 [NEXT: Go to Paramiko examples](https://github.com/mikesaur/public/tree/master/Python_101/paramiko)

 