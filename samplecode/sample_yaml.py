import yaml
from pprint import pprint

# YAMLファイルの読み込み
file = open("sample_yaml.yml", "r")

# fileオブジェクトからYAMLを読み込み、変数に格納
router_info = yaml.load(file)

pprint(router_info)

print(router_info['host_info']['hostname'])
print(router_info['if_info']['if_name'])