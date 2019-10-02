https://pynet.twb-tech.com/blog/automation/netmiko-grep.html

1. Test your yaml file: 
```netmiko-grep --list-devices```

2. Search all routers running-config for a string: 
```netmiko-grep --cmd 'show run' '1.1.1.1' all```

3. Search all XE routers running-config for a string: 
```netmiko-grep --cmd 'show run' '1.1.1.1' xe_devices``` 
