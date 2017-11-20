# Exscript
Exscript
- https://github.com/knipknap/exscript


# Install 

```
pip3 install exscript
```

# Router show

```python
import Exscript

username = 'user1'
password = 'password1'
ip4 = '192.168.33.3'

# SSHセッションの確立
session = Exscript.protocols.SSH2()
session.connect(ip4)

# ルータにログイン
account = Exscript.Account(name=username, password=password)
session.login(account)

# ルータにコマンドを送信、出力結果を取得
session.execute('show configuration interfaces ge-0/0/1')
result = session.response
print(result)

# SSHセッションの切断
if session:
    session.send('exit\r')
    session.close()
else:
    raise AttributeError('Cannot find a livied session')
```

```
$ python3 sample_exscript.py

show configuration interfaces ge-0/0/1
unit 0 {
    family inet {
        address 192.168.33.3/24;
    }
}
```

# Router set configure
