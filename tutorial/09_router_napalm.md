# NAPALM

# Install 

```
pip3 install napalm
```

# router show interface

```python
import napalm
from pprint import pprint

driver = napalm.get_network_driver('junos')
device = driver(
    hostname='192.168.33.3',
    username='user1',
    password='password1' )

device.open()

interface_dict = device.get_interfaces()
pprint(interface_dict)
pprint(interface_dict["ge-0/0/2"])

interface_ip_dict = device.get_interfaces_ip()
pprint(interface_ip_dict)
pprint(interface_ip_dict["ge-0/0/2.0"])

device.close()
```

```
$ python3 sample_napalm.py

{'.local.': {'description': '',
             'is_enabled': True,
             'is_up': True,
             'last_flapped': -1.0,
             'mac_address': 'Unspecified',
             'speed': -1},
 'dsc': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'Unspecified',
         'speed': -1},
 'ge-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': 1640.0,
              'mac_address': '08:00:27:AE:F4:51',
              'speed': 1000},
 'ge-0/0/1': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': 1641.0,
              'mac_address': '08:00:27:15:4F:F5',
              'speed': 1000},
 'ge-0/0/2': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': 1272.0,
              'mac_address': '08:00:27:1D:63:CE',
              'speed': 1000},
 'gr-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': -1.0,
              'mac_address': 'None',
              'speed': 800},
 'gre': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'None',
         'speed': -1},
 'ip-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': -1.0,
              'mac_address': 'None',
              'speed': 800},
 'ipip': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': -1},
 'irb': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': '4C:96:14:10:01:30',
         'speed': -1},
 'lo0': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'Unspecified',
         'speed': -1},
 'lsi': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'Unspecified',
         'speed': -1},
 'lsq-0/0/0': {'description': '',
               'is_enabled': True,
               'is_up': True,
               'last_flapped': 1641.0,
               'mac_address': 'None',
               'speed': -1},
 'lt-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': -1.0,
              'mac_address': '02:96:14:10:01:33',
              'speed': 800},
 'mt-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': -1.0,
              'mac_address': 'None',
              'speed': 800},
 'mtun': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': -1},
 'pimd': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': -1},
 'pime': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': -1},
 'pp0': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'Unspecified',
         'speed': -1},
 'ppd0': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': 800},
 'ppe0': {'description': '',
          'is_enabled': True,
          'is_up': True,
          'last_flapped': -1.0,
          'mac_address': 'None',
          'speed': 800},
 'sp-0/0/0': {'description': '',
              'is_enabled': True,
              'is_up': True,
              'last_flapped': 1641.0,
              'mac_address': 'Unspecified',
              'speed': 800},
 'st0': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'None',
         'speed': -1},
 'tap': {'description': '',
         'is_enabled': True,
         'is_up': True,
         'last_flapped': -1.0,
         'mac_address': 'Unspecified',
         'speed': -1},
 'vlan': {'description': '',
          'is_enabled': True,
          'is_up': False,
          'last_flapped': 1652.0,
          'mac_address': '00:00:00:00:00:00',
          'speed': 1000}}

{'description': '',
 'is_enabled': True,
 'is_up': True,
 'last_flapped': 1272.0,
 'mac_address': '08:00:27:1D:63:CE',
 'speed': 1000}

{'ge-0/0/0.0': {'ipv4': {'10.0.2.15': {'prefix_length': 24}}},
 'ge-0/0/1.0': {'ipv4': {'192.168.33.3': {'prefix_length': 24}}},
 'ge-0/0/2.0': {'ipv4': {'192.168.33.4': {'prefix_length': 24}}},
 'lo0.16384': {'ipv4': {'127.0.0.1': {'prefix_length': 32}}},
 'lo0.16385': {'ipv4': {'10.0.0.1': {'prefix_length': 32},
                        '10.0.0.16': {'prefix_length': 32},
                        '128.0.0.1': {'prefix_length': 32},
                        '128.0.0.4': {'prefix_length': 32},
                        '128.0.1.16': {'prefix_length': 32}}},
 'sp-0/0/0.16383': {'ipv4': {'10.0.0.1': {'prefix_length': 32},
                             '10.0.0.6': {'prefix_length': 32},
                             '128.0.0.1': {'prefix_length': 32},
                             '128.0.0.6': {'prefix_length': 32}}}}

{'ipv4': {'192.168.33.4': {'prefix_length': 24}}}
```

# 

# Reference
https://napalm.readthedocs.io/en/latest/
