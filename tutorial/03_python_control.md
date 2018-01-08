# if

```python
num = 2

if num == 1:
    print("num is one")
elif num == 2:
    print("num is two")
else:
    print("num is the others")
```

```
$ python3 sample_if.py

num is two
```

# for

```python
# リスト型変数を利用して繰り返し処理を実施
router_list = ['router_A', 'router_B', 'router_C']
# router_listの値を、順次 router_name に代入
for router_name in router_list:
    print(router_name)

# 繰り返し回数を指定して繰り返し処理を実施
# range(5) = 0,1,2,3,4が格納
for num in range(5): 
    print(num)
```

```
$ python3 sample_for.py

router_A
router_B
router_C
0
1
2
```


# function

```python
# 関数の定義
# ルータ情報を受けとり、OSに応じたshow bgp summaryコマンドを返すコマンド
def get_show_bgp_summary(router_info):
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
command = get_show_bgp_summary(router_info)
print(command)
```

```
$ python3 samplecode/sample_function.py

show bgp summary
```

# class

```python
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
```

```
$ python3.6 sample_class.py

router_A
show bgp summary
router_B
show ip bgp summary
```

# open file

```python
file1 = open("sample_read.txt", "r")
text = file1.read() # ファイル全文を文字列として読み込み
#text = file1.readline() # ファイル1行目のみを文字列として読み込み
#text = file1.readlines() # ファイルを行ごとに配列として読み込み
print(text)

file2 = open("sample_write.txt", "w")
file2.write("Good!")
file2.close
```

```
$ python3 sample_file.py

Hello JANOG! from sample_read.txt
How are you feeling?
```