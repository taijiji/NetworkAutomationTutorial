class Router:
    # クラス変数(全インスタンス共通で設定される)
    router = {
        "router_name"   : "",
        "ip"            : "",
        "os"            : "",
    }

    def set_router_name(self, router_name):
        self.router["router_name"] = router_name
    
    def get_router_name(self):
        return self.router["router_name"]
        
router_A = Router()
router_A.set_router_name("Router A")

router_name = router_A.get_router_name()

print(router_name)