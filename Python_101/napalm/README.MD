https://napalm.readthedocs.io/en/latest/index.html<br>

Config push<br>
- Change in to the Napalm directory:<br>
```cd ../napalm```<br>

- IOS-XR Push config:<br>
- Prior to executing this script update the 1_config_napalm.txt file in the napalm directory.<br>
    - Change the number 2100 in all spots to a random but valid 4 digit VLAN number.<br>
    - Execute the script:<br>
 ```python 1_push_config.py XRv01_LAB```<br>

- IOS-XE Push config:<br>
- Prior to executing this script update the 2_config_napalm.txt file in the napalm directory.<br>
    - Change the number name-server IP to a random but valid IPv4 address.<br>
    - Execute the script:<br>
 ```python 2_push_config.py XE01_LAB```<br>

---
Config rollback<br>

- IOS-XR Rollback:<br>
 ```python xr_rollback.py XRv01_LAB```<br>

- IOS-XE Rollback:<br>
 ```python xe_rollback.py XE01_LAB```<br>

---

Napalm Command Line Tool<br>

```napalm --user cisco --password cisco --vendor iosxr XRv01_LAB call get_interfaces_counters```<br>
```napalm --user cisco --password cisco --vendor ios XE01_LAB call get_snmp_information```

More Built-in calls: https://napalm.readthedocs.io/en/latest/support/index.html

