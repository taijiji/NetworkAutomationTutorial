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
$ python3 sample_napalm_show.py

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
# For NAPALM
import napalm
# For Color Font
from colorama import init as colorama_init
from colorama import Fore

colorama_init(autoreset=True)

driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

device.open()

print("===== Step 1. run show command =====")
print("Interface Status:  ", end="") 
if device.get_interfaces()["ge-0/0/1"]["is_up"] == True:
    status_before = "up"
elif device.get_interfaces()["ge-0/0/1"]["is_up"] == False:
    status_before = "down"
print(Fore.YELLOW + status_before)

print("===== Step 2. configure =====")
device.load_merge_candidate(filename="./sample_config_junos.txt")
print("OK")

print("===== Step 3. compare configuration =====")
print(Fore.YELLOW + device.compare_config())

print("===== Step 4. commit =====")
print("Do you commit? y/n")
choice = input()
if choice == "y":
    print("Commit config: ", end="")
    device.commit_config()
    print("OK")
else:
    print("Discard config: ", end="")
    device.discard_config()
    print("OK")

print("===== Step 5. run show command(again) =====")
print("Interface Status:  ", end="") 
if device.get_interfaces()["ge-0/0/1"]["is_up"] == True:
    status_after = "up"
elif device.get_interfaces()["ge-0/0/1"]["is_up"] == False:
    status_after = "down"
print(Fore.YELLOW + status_after)

device.close()
```


``` 
$ python3 sample_napalm_set.py

===== Step 1. run show command =====
Interface Status:  up
===== Step 2. configure =====
OK
===== Step 3. compare configuration =====
[edit interfaces ge-0/0/1]
+   disable;
===== Step 4. commit =====
Do you commit? y/n
n
Discard config: OK
===== Step 5. run show command(again) =====
Interface Status:  up
```

# Reference
https://napalm.readthedocs.io/en/latest/
