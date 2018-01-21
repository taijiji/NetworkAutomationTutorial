# For NAPALM
import napalm
# For Color Font
from colorama import init as colorama_init
from colorama import Fore
# For sleep
import time

colorama_init(autoreset=True)

driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

device.open()

print("===== Step 1. run show command =====")
print("Interface Status:  ", end="") 
result_before = device.get_interfaces()["ge-0/0/1"]["is_up"]
if result_before == True:
    status_before = "UP"
elif result_before == False:
    status_before = "DOWN"
print(Fore.YELLOW + status_before)
print("===== Step 2. configure =====")
device.load_merge_candidate(filename="./sample_config_junos.txt")
print("OK")

print("===== Step 3. compare configuration =====")
print(Fore.YELLOW + device.compare_config())

print("===== Step 4. commit =====")
print(Fore.YELLOW + "Do you commit? y/n")
choice = input()
if choice == "y":
    print("Commit config: ", end="")
    device.commit_config()
    print(Fore.YELLOW + "OK")
else:
    print("Discard config: ", end="")
    device.discard_config()
    print(Fore.YELLOW + "OK")

time.sleep(3) # interface shutdown実行完了を待つ処理。

print("===== Step 5. run show command(again) =====")
print("Interface Status:  ", end="")
result_after = device.get_interfaces()["ge-0/0/1"]["is_up"]
if result_after  == True:
    status_after = "UP"
elif result_after == False:
    status_after = "DOWN"
print(Fore.YELLOW + status_after)

device.close()