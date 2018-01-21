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