import napalm
from pprint import pprint

driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

print("Open session: ")
device.open()
print("OK")

print("Interface ge-0/0/2 Status:  ") 
print(device.get_interfaces()["ge-0/0/2"]["is_up"])

print("Config load (merge mode): ")
device.load_merge_candidate(filename="./sample_config_junos.txt")
print("OK")

print("Compare config: ")
print(device.compare_config())

print("Do you commit? y/n")
choice = input()
if choice == "y":
    print("Commit config:")
    device.commit_config()
    print("OK")
else:
    print("Discard config:")
    device.discard_config()
    print("OK")

print("Interface ge-0/0/2 Status:  ") 
print(device.get_interfaces()["ge-0/0/2"]["is_up"])

print("Close session: ")
device.close()
print("OK")