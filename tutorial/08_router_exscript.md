# Exscript
Exscript
- https://github.com/knipknap/exscript


# Install 

```
pip3 install exscript
```

# Router show

```python
import Exscript # SSHライブラリ
import re       # 正規表現ライブラリ

username = "user1"
password = "password1"
ip4 = "192.168.33.3"

# SSHセッションの確立
session = Exscript.protocols.SSH2()
session.connect(ip4)

# ルータにログイン
account = Exscript.Account(name=username, password=password)
session.login(account)

# ルータにコマンドを送信、出力結果を取得
session.execute("show version")
result = session.response
print(result)
print("----------")

# 正規表現で情報抽出
regex = "JUNOS Software Release \[(.+)\]"
match = re.search(regex, result)
version = match.group(1)
print(version)

# SSHセッションの切断
session.send("exit")
session.close()
```

```
$ python3 sample_exscript_show.py

show version
Hostname: vsrx
Model: firefly-perimeter
JUNOS Software Release [12.1X47-D15.4]
----------
12.1X47-D15.4
```

# Router set configure

```python

# For SSH
import Exscript
# For Color Font
from colorama import init as colorama_init
from colorama import Fore

colorama_init(autoreset=True)

username = "user1"
password = "password1"
ip4 = "192.168.33.3"

# SSHセッションの確立
session = Exscript.protocols.SSH2()
session.connect(ip4)

# ルータにログイン
account = Exscript.Account(name=username, password=password)
session.login(account)

print("===== Step 1. run show command =====")
session.execute("show configuration interfaces ge-0/0/1")
print(Fore.YELLOW + session.response)

print("===== Step 2. configure =====")
session.execute("configure")

config_txt = "set interfaces ge-0/0/1 disable"
session.execute(config_txt)
print(Fore.YELLOW + session.response)

print("===== Step 3. commit check =====")
session.execute("show | compare")
print(Fore.YELLOW + session.response)
session.execute("commit check")
print(session.response)

print("===== Step 4. commit =====")
# ユーザにy or nを質問
print(Fore.YELLOW + "Do you commit? y/n")
choice = input()
if choice == "y":
    session.execute("commit")
    print(session.response)
else:
    session.execute("rollback")
    print(session.response)

session.execute("exit")
print(session.response)

print("===== Step 5. run show command(again) =====")
session.execute("show configuration interfaces ge-0/0/1")
print(Fore.YELLOW + session.response)

session.send("exit")
session.close()
```


```
$ python3 sample_exscript_set.py

===== Step 1. run show command =====
show configuration interfaces ge-0/0/1
unit 0 {
    family inet {
        address 10.0.1.1/24;
    }
}
===== Step 2. configure =====
set interfaces ge-0/0/1 disable
===== Step 3. commit check =====
show | compare
[edit interfaces ge-0/0/1]
+   disable;
commit check
configuration check succeeds
===== Step 4. commit =====
Do you commit? y/n
y
commit
commit complete
exit
Exiting configuration mode
===== Step 5. run show command(again) =====
show configuration interfaces ge-0/0/1
disable;
unit 0 {
    family inet {
        address 10.0.1.1/24;
    }
}
```