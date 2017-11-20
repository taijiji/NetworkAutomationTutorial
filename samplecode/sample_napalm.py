import napalm
from pprint import pprint

driver = napalm.get_network_driver('junos')
device = driver(
    hostname='192.168.33.3',
    username='user1',
    password='password1' )

device.open()

interface_dict = device.get_interfaces()
pprint(interface_dict["ge-0/0/2"])

interface_ip_dict = device.get_interfaces_ip()
#pprint(interface_ip_dict)
pprint(interface_ip_dict["ge-0/0/2.0"])

device.close()