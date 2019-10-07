https://napalm.readthedocs.io/en/latest/index.html<br>

Config push<br>

- IOS-XR Push config: ```python 1_push_config.py xr_routername```

- IOS-XE Push config: ```python 2_push_config.py xe_routername```

---
Config rollback<br>

- IOS-XR Rollback: ```python xr_rollback.py xr_routername```

- IOS-XE Rollback: ```python xe_rollback.py xe_routername```

---

Napalm Command Line Tool<br>

```napalm --user cisco --password cisco --vendor iosxr XRv01_LAB call get_interfaces_counters```<br>
```napalm --user cisco --password cisco --vendor ios XE01_LAB call get_snmp_information```

Built-in calls: https://napalm.readthedocs.io/en/latest/support/index.html

[NEXT: Go to Napalm examples](https://github.com/mikesaur/public/tree/master/Python_101/napalm)
