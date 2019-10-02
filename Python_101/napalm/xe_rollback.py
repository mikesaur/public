import sys
from napalm.base import get_network_driver
driver = get_network_driver('ios')

router = sys.argv[1]
print('Rolling back configuration on: ' + router)

dev = driver(hostname=router, username='cisco',
             password='cisco')
dev.open()
dev.rollback()
dev.close()