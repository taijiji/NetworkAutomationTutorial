import json


file = open("sample_json.json", "r")

# fileオブジェクトからjsonを読み込み、変数に格納
routers_list = json.load(file)

# fileオブジェクトから一旦文字列オブジェクトに読みこみ、その後jsonを読み込み
#file = open("sample_json.json", "r")
#routers_txt = file.read()
#print(routers_txt)
#routers_list = json.loads(routers_txt)

print(routers_list)
print(type(routers_list))