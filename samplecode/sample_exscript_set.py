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
session.execute("show configuration interfaces ge-0/0/1")
result = session.response
print(result)

print("="*40)
print("Step 3. run configure command")
print("="*40)
session.execute("configure")

config_txt = "set interfaces ge-0/0/1 disable"
session.execute(config_txt)
result = session.response
print(result)

print("="*40)
print("Step 4. commit check")
print("="*40)
session.execute("show | compare")
result = session.response
print(result)
session.execute("commi check")
result = session.response
print(result)


print("="*40)
print("Step 5. commit")
print("="*40)
print("Do you commit? y/n")
choice = raw_input().lower()
if choice == "y":
    session.execute("commit")
    print session.response
else:
    session.execute("rollback")
    print session.response
session.execute("exit")
result = session.response
print(result)


print("="*40)
print("Step 6. run show command(again)")
print("="*40)
session.execute("show configuration interfaces ge-0/0/1")
result = session.response
print(result)


if session:
    session.send("exit\r")
    session.close()
else: