# 関数の定義
# ルータ情報を受けとり、OSに応じたshow bgp summaryコマンドを返すコマンド
def get_show_bgp_summary_command(router_info):
    if router_info["os"] == "junos":
        command = "show bgp summary"
    elif router_info['os'] == 'ios':
        command = "show ip bgp summary"
    else:
        command = 'N/A'
    return command

# 辞書型変数
router_info = {
    "hostname"  : "router_A",
    "os"        : "junos",
    "version"   : "15.1"
}

# router_infoを引数として、関数を呼び出し
command = get_show_bgp_summary_command(router_info)
print(command)