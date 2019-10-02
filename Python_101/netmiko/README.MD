https://pynet.twb-tech.com/blog/automation/netmiko-grep.html<br><br>
https://pynet.twb-tech.com/blog/automation/netmiko-tools.html

---
Grep your whole network:<br>
1. Test your yaml file<br> 
```netmiko-grep --list-devices```

2. Search all routers running-config for a string<br>
```netmiko-grep --cmd 'show run' '1.1.1.1' all```

3. Search all XE routers running-config for a string:<br> 
```netmiko-grep --cmd 'show run' '1.1.1.1' xe_devices``` 

---

