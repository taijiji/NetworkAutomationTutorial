import Exscript

#from Exscript.protocols import SSH2
#from Exscript.Account import Account

username = 'user1'
password = 'pass1'
ip4 = '192.168.33.3'

# SSHセッションの確立
session = Exscript.protocols.SSH2()
session.connect(ip4)

# ルータにログイン
account = Exscript.Account.Account(name=username, password=password)
session.login(account)

# ルータにコマンドを送信、出力結果を取得
session.execute('show configuration interfaces xe-0/0/0 | no-more')
print session.response


# SSHセッションの切断
if session:
    session.send('exit\r')
    session.close()
else:
    raise AttributeError('Cannot find a livied session')