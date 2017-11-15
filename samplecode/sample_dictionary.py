# 「key」と「value」のペアを変数として定義
router_info = {
    "hostname"  : "router_A",
    "os"        : "junos",
    "ip"        : "192.168.0.1" 
}

print(router_info) # 辞書型変数を表示

# 「key」が "hostname" の場合の、「value」を表示
print(router_info["hostname"]) 

#　「key」が"ip"の場合の、「value」を別の値に変更
router_info["ip"] = "192.168.0.2"
print(router_info)