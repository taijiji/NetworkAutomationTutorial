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
pattern = "JUNOS Software Release \[(.+)\]"
match = re.search(pattern, result)
version = match.group(1)
print(version)

# SSHセッションの切断
session.send("exit")
session.close()