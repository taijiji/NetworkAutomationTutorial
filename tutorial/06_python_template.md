# template engine by jinja2

```
pip install jinja2
```

```python
import jinja2

file = open("sample_template.jinja2", "r")
template_txt = file.read()
print(template_txt)

# １つのテンプレート(雛形)から１つのテキストファイルを作成する例
template = jinja2.Environment().from_string(template_txt)
config_txt = template.render(
    if_description="To_RouterA",
    if_name="fastethernet 1/1",
    ip4='192.168.0.1',
    ip4_subnet="255.255.255.0")
print(config_txt)

# １つのテンプレート(雛形)から複数のテキストファイルを作成する例
interfaces = [
    {
        "if_description" : "To_RouterA",
        "if_name" : "fastethernet 1/1",
        "ip4" : "192.168.0.1",
        "ip4_subnet" : "255.255.255.0"
    },
    {
        "if_description" : "To_RouterB",
        "if_name" : "fastethernet 1/2",
        "ip4" : "192.168.1.1",
        "ip4_subnet" : "255.255.255.0"
    },
    {
        "if_description" : "To_RouterC",
        "if_name" : "fastethernet 1/3",
        "ip4" : "192.168.2.1",
        "ip4_subnet" : "255.255.255.0"
    }
]

for interface in interfaces:
    config_txt = template.render(interface)
    print(config_txt)
```

```
$ python3 sample_template.py

interface {{ if_name }}
 description {{ if_description }}
 ip address {{ ip4 }} {{ ip4_subnet }}
 duplex auto
 speed auto
 no shutdown
!


interface fastethernet 1/1
 description To_RouterA
 ip address 192.168.0.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!


interface fastethernet 1/1
 description To_RouterA
 ip address 192.168.0.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
interface fastethernet 1/2
 description To_RouterB
 ip address 192.168.1.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
interface fastethernet 1/3
 description To_RouterC
 ip address 192.168.2.1 255.255.255.0
 duplex auto
 speed auto
 no shutdown
!
```