https://pynet.twb-tech.com/blog/automation/netmiko-tools.html

---
Grep your whole network!<br>

Change to the Netmiko directory:<br>
```cd ../netmiko```<br>

Test your yaml file first:<br> 
```./netmiko-grep --list-devices```

Search all routers running-config for a string:<br>
```./netmiko-grep --cmd 'show run' '1.1.1.1' all```

Search all XE routers running-config for a string:<br> 
```./netmiko-grep --cmd 'show run' '1.1.1.1' xe_devices``` 

---
Push config snippets from a file:<br>
    - In Windows open SublimeText3 (or other code editor)<br>
    - In SublimeText3 go to: File --> Open Folder<br>
        - Browse your desktop, linux file system shortcut, then the "Python_101" folder<br>
        - In SublimeText3 on the left you should see the netmiko folder<br>
        - Choose the drop-down triangle to show files in the netmiko folder<br>
        - Click on the 'xeconfig.txt' file to edit<br>
        - You'll see 2 ntp servers<br> 
        - Randomly type 2 different ones (any valid IPv4 addresses)<br>
        - Save the file <br>
    - Execute the config lines below to run netmiko-cfg tool <br>
     
```./netmiko-cfg --infile xeconfig.txt xe_devices```<br><br>
```./netmiko-cfg --cmd 'ntp server 15.15.15.15' xe_devices```

---
Run show command across the network.<br>
```./netmiko-show --cmd "show run | i ntp" xe_devices```

[NEXT: Go to Napalm examples](https://github.com/mikesaur/public/tree/master/Python_101/napalm)
