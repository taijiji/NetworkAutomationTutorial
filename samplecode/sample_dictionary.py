# 「key」と「value」のペアを変数として定義
router_info = {
    "hostname"  : "router_A",
    "os"        : "junos",
    "version"   : "15.1",
    "ip"        : "192.168.0.1",
}

print(router_info) # 辞書型変数を表示

# ホスト名を表示
print(router_info["hostname"]) 

# バージョンを表示
print(router_info["version"]) 


#　「key」が"ip"の場合の、「value」を別の値に変更
router_info["ip"] = "192.168.0.2"
print(router_info)