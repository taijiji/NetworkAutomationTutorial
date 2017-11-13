# json

```python
import json

# fileオブジェクトからjsonを読み込み
file = open("sample_json.json", "r")
routers_list = json.load(file)

# fileオブジェクトから一旦文字列オブジェクトに読みこみ、その後jsonを読み込み
#file = open("sample_json.json", "r")
#routers_txt = file.read()
#print(routers_txt)
#routers_list = json.loads(routers_txt)

print(routers_list)
print(type(routers_list))
```

```
$ python3 sample_json.py

[{'router_name': 'Router_A', 'ip': '192.168.0.1', 'os': 'junos'}, {'router_name': 'Router_B', 'ip': '192.168.0.2', 'os': 'ios'}, {'router_name': 'Router_C', 'ip': '192.168.0.3', 'os': 'iosxr'}]

<class 'list'>
```