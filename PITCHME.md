# 明日からはじめるネットワーク運用自動化 始動編
- 2018/1/9 10:00-12:00JST
- Taiji Tsuchiya / 土屋 太二
- ITOCHU Techno-Solutions America, Inc.
- NetOpsCoding Committee

---

# 自己紹介
- 土屋 太二/Taiji Tsuchiya
- Career
  - Solution Engineer @ CTC America (2017-Present)
    - 米国展開している日本企業の技術支援
    - グローバル企業のネットワーク/インフラ技術の調査
    - アプリケーションソフトウェアのプロトタイピング
  - Network Engineer @ BIGLOBE (2011-2017)
    - DC/バックボーン/Peeringの運用/設計/開発
    - ネットワーク運用自動化システム、SDNシステムの開発
- Community Activities
  - NetOpsCoding 運営委員
  - 過去JANOG プログラム委員, 実行委員長など

---

# 目次
本発表では、プログラミング言語としてPython(3系)を例にします。

- Python入門
- 変数
- if文
- for文
- 関数
- ファイル入出力
- JSON
- テンプレートエンジン
- 正規表現
- テスト
- 開発に便利なOSSライブラリ/ツールの紹介
- やってみようネットワーク自動化
- プログラムからルータにログイン、showコマンドを実行
- プログラムからルータにコンフィグ投入
- 自動化サンプル: BGP Peering作業を自動化する

---

# 変数(辞書型)
辞書型変数 = { キー1:バリュー1, キー2:バリュー2, … }

```python
# 「key : value」のペアを変数として定義
routerA_info = {
    "hostname"  : "router_A",
    ”os"         : ”junos" 
}

print(routerA_info) # 辞書型変数を表示

# 「key = “hostname”」の場合の、「value」を表示
print(routerA_info["hostname"])
```

```
$ python3 sample_dictionary.py

{'hostname': 'router_A', ’os': ’junos'}
router_A
```

----

# クラス

```python
class Router:
    # クラス変数(全インスタンス共通で設定される変数)
    router = {
        "router_name"   : "",
        "ip"            : "",
        "os"            : ""
    }

    # クラス内の関数の定義。ルータ名の設定
    def set_router_name(self, router_name):
        self.router["router_name"] = router_name
    
    # クラス内の関数の定義。ルータ名の取得
    def get_router_name(self):
        return self.router["router_name"]

# Routerクラスのインスタンスを生成        
router_A = Router()

# Routerクラスで定義された関数を呼び出し
router_A.set_router_name("Router A")
router_name = router_A.get_router_name()

print(router_name) # => 「Router A」が表示

```

---

# Thanks!