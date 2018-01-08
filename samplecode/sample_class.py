class Router:
    # 初期化関数: インスタンス生成時に必ず呼ばれる関数。
    def __init__(self, hostname, os, version):
        # インスタンス変数: 各インスタンスで利用できる変数。
        self.hostname   = hostname
        self.os         = os
        self.version    = version

    # 関数の定義。show bgp summaryコマンドを返す。
    def get_show_bgp_summary(self):
        if self.os == "junos":
            command = "show bgp summary"
        elif self.os == 'ios':
            command = "show ip bgp summary"
        else:
            command = 'N/A'
        return command

# Routerクラスのインスタンスを生成
router_A = Router(hostname="router_A", os="junos", version="15.1")
router_B = Router(hostname="router_B", os="ios", version="15.7(3)M")

# それぞれのインスタンスでRouterクラスで定義された関数を呼び出し
router_A_command = router_A.get_show_bgp_summary()
print(router_A.hostname)
print(router_A_command)

router_B_command = router_B.get_show_bgp_summary()
print(router_B.hostname)
print(router_B_command)
