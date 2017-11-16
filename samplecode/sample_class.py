class Router:
    # クラス変数(全インスタンス共通で設定される変数)
    router = {
        "router_name"   : "",
        "ip"            : "",
        "os"            : "",
    }

    # 関数の定義。ルータ名の設定
    def set_router_name(self, router_name):
        self.router["router_name"] = router_name
    
    # 関数の定義。ルータ名の取得
    def get_router_name(self):
        return self.router["router_name"]

# Routerクラスのインスタンスを生成        
router_A = Router()

# Routerクラスで定義された関数を呼び出し
router_A.set_router_name("Router A")
router_name = router_A.get_router_name()

print(router_name)