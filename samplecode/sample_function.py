# 関数の定義
# ルータ名の配列を受けとり、表示させる関数
def test_function(router_list):
    for router_name in router_list:
        print(router_name)

router_list = ['router_A', 'router_B', 'router_C', 'router_D']
# 関数の呼び出し
test_function(router_list)