https://napalm.readthedocs.io/en/latest/index.html<br>

Config push<br>
- Change in to the Napalm directory:<br>
```cd ../napalm```<br>

- IOS-XR Push config:<br>
 ```python 1_push_config.py xr_routername```<br>

- IOS-XE Push config:<br>
 ```python 2_push_config.py xe_routername```<br>

---
Config rollback<br>

- IOS-XR Rollback:<br>
 ```python xr_rollback.py xr_routername```<br>

- IOS-XE Rollback:<br>
 ```python xe_rollback.py xe_routername```<br>

---

Napalm Command Line Tool<br>

```napalm --user cisco --password cisco --vendor iosxr XRv01_LAB call get_interfaces_counters```<br>
```napalm --user cisco --password cisco --vendor ios XE01_LAB call get_snmp_information```

Built-in calls: https://napalm.readthedocs.io/en/latest/support/index.html

