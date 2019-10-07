https://pynet.twb-tech.com/blog/automation/netmiko-tools.html

---
Grep your whole network!<br>

Test your yaml file first:<br> 
```./netmiko-grep --list-devices```

Search all routers running-config for a string:<br>
```./netmiko-grep --cmd 'show run' '1.1.1.1' all```

Search all XE routers running-config for a string:<br> 
```./netmiko-grep --cmd 'show run' '1.1.1.1' xe_devices``` 

---
Push config snippets from a file:<br>
```./netmiko-cfg --infile xeconfig.txt xe_devices```<br><br>
```./netmiko-cfg --cmd 'ntp server 15.15.15.15' xe_devices```

---
Run show command across the network.<br>
```./netmiko-show --cmd "show run | i ntp" xe_devices```

