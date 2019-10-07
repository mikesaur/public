Here are some sample scripts for starting out with Python for Network Engineers<br>
There are so many great modules out there to leverage.

Install Tools

Step 1: Install Windows Subsystem for Linux (WSL)<br>
<i>Note: I suggest Ubuntu</i><br>

- Instructions: ```https://docs.microsoft.com/en-us/windows/wsl/install-win10```

Step 2: Install unzip: ```sudo apt-get install unzip```

Step 3: Clone repository: ```git clone https://github.com/mikesaur/public.git```

Step 4: Move in to the Python_101 directory: ```cd public/Python_101```

Step 5: Install Python package manager:<br>
    - ```sudo apt update```<br>
    - ```sudo apt upgrade``` #Need to see if I really need to do this.<br>
    - ```sudo apt install python3-pip```<br>
    
Step 5: Install python virtual environment: ```sudo apt-get install virtualenv```

Step 6: Setup a virtual environment:<br>
    -  ```virtualenv -p python3 venv```<br>
    - ```source venv/bin/activate```
 
  

 