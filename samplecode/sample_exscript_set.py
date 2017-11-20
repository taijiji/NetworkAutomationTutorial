import Exscript

username = "user1"
password = "password1"
ip4 = "192.168.33.3"

# SSHセッションの確立
session = Exscript.protocols.SSH2()
session.connect(ip4)

# ルータにログイン
account = Exscript.Account(name=username, password=password)
session.login(account)

print("="*40)
print("Step 1. run show command")
print("="*40)
session.execute("show configuration interfaces ge-0/0/2")
print(session.response)


print("="*40)
print("Step 2. configure")
print("="*40)
session.execute("configure")

config_txt = "set interfaces ge-0/0/2 disable"
session.execute(config_txt)
print(session.response)

print("="*40)
print("Step 3. commit check")
print("="*40)
session.execute("show | compare")
print(session.response)
session.execute("commi check")
print(session.response)

print("="*40)
print("Step 4. commit")
print("="*40)
print("Do you commit? y/n")
choice = input()
if choice == "y":
    session.execute("commit")
    print(session.response)
else:
    session.execute("rollback")
    print(session.response)

session.execute("exit")
print(session.response)


print("="*40)
print("Step 6. run show command(again)")
print("="*40)
session.execute("show configuration interfaces ge-0/0/2")
print(session.response)

session.send("exit")
session.close()