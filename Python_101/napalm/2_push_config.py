import sys
from napalm.base import get_network_driver
driver = get_network_driver('ios')


router = sys.argv[1]
print('Configuring: ' + router)


dev = driver(hostname=router, username='cisco',
             password='cisco')
dev.open()
dev.load_merge_candidate(filename='2_config_napalm.txt')
diffs = dev.compare_config()
if len(diffs) > 0:
    print(diffs)
    dev.commit_config()
else:
    print('No changes needed')
    dev.discard_config()

dev.close()