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
```

```
$ python3 samplecode/sample_function.py

show bgp summary
```

# class
```python
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
        router_name = self.router["router_name"]
        return router_name
        
router_A = Router()
router_A.set_router_name("Router A")

router_name = router_A.get_router_name()

print(router_name)
```

```
$ python3 sample_class.py

Router A
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