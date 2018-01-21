# NAPALM

# Install 

```
pip3 install napalm
```

# router show version

```python
 # NAPALM ライブラリ
 # 要: pip3 install napalm)
import napalm
from pprint import pprint

# JUNOS用インスタンスを生成
driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

# コネクションの確率
device.open()

# 基本情報の取得
fact = device.get_facts()
pprint(fact) # pprint: 辞書型変数を人に見やすく表示

print("----------")

# バージョンの取得(基本情報から抽出)
print(fact["os_version"])
device.close()
```

```
python3 sample_napalm_show.py
{'fqdn': 'vsrx',
 'hostname': 'vsrx',
 'interface_list': ['ge-0/0/0',
                    'gr-0/0/0',
                    'ip-0/0/0',
                    'lsq-0/0/0',
                    'lt-0/0/0',
                    'mt-0/0/0',
                    'sp-0/0/0',
                    'ge-0/0/1',
                    'ge-0/0/2',
                    '.local.',
                    'dsc',
                    'gre',
                    'ipip',
                    'irb',
                    'lo0',
                    'lsi',
                    'mtun',
                    'pimd',
                    'pime',
                    'pp0',
                    'ppd0',
                    'ppe0',
                    'st0',
                    'tap',
                    'vlan'],
 'model': 'FIREFLY-PERIMETER',
 'os_version': '12.1X47-D15.4',
 'serial_number': '83f144ddd4f7',
 'uptime': 8309,
 'vendor': 'Juniper'}
----------
12.1X47-D15.4
```

# Routour Configure

```python
import napalm
from pprint import pprint

driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

print("Open session: ")
device.open()
print("OK")

print("Interface ge-0/0/2 Status:  ") 
print(device.get_interfaces()["ge-0/0/2"]["is_up"])

print("Config load (merge mode): ")
device.load_merge_candidate(filename="./sample_config_junos.txt")
print("OK")

print("Compare config: ")
print(device.compare_config())

print("Do you commit? y/n")
choice = input()
if choice == "y":
    print("Commit config:")
    device.commit_config()
    print("OK")
else:
    print("Discard config:")
    device.discard_config()
    print("OK")

print("Interface ge-0/0/2 Status:  ") 
print(device.get_interfaces()["ge-0/0/2"]["is_up"])

print("Close session: ")
device.close()
print("OK")
```


```
Open session:
OK
Interface ge-0/0/2 Status:
True
Config load (merge mode):
OK
Compare config:
[edit interfaces ge-0/0/2]
+   disable;
Do you commit? y/n
y
Commit config:
OK
Interface ge-0/0/2 Status:
True
Close session:
OK
```

# Reference
https://napalm.readthedocs.io/en/latest/
