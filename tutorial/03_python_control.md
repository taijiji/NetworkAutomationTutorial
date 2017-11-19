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
def test_function(router_list):
    
    for router_name in router_list:
        print(router_name)

router_list = ['router_A', 'router_B', 'router_C', 'router_D']
test_function(router_list)
```

```
$ python3 sample_function.py

router_A
router_B
router_C
router_D
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