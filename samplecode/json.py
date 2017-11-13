import json

file = open("sample_json.json", "r")
routers_txt = file.read()
# print(type(routers_txt))
print(routers_txt)

# routers_list = json.load(file)
routers_list = json.load(router_txt)
print(routers_list)