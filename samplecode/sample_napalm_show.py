 # NAPALM ライブラリ
 # 要: pip3 install napalm)
import napalm
from pprint import pprint

# JUNOS用インスタンスを生成
driver = napalm.get_network_driver("junos")
device = driver(
    hostname="192.168.33.3",
    username="user1",
    password="password1" )

# コネクションの確立
device.open()

# 基本情報の取得
#fact = device.get_facts()
#pprint(fact) # pprint: 辞書型変数を人に見やすく表示

#print("----------")

# バージョンの取得(基本情報から抽出)
#print(fact["os_version"])

print(device.get_interfaces()["ge-0/0/0"]["is_up"])

device.close()