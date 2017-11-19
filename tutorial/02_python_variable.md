# print

```python
print("Hello World!")
```

```
$ python3 sample_print.py

Hello World!
```

# Variable

Pythonでは、型の指定(「int a;」「float b;」など)は必要なく、自動で型が判定されます。

## 数値型

```python
a = 1   # a: int型として生成
b = 1.1 # b: float型として生成
print(a)
print(b)
print(type(a))
print(type(b))

c = a + b # c: float型として生成
print(c)
print(type(c))
```

```
$ python3 sample_number.py

1
1.1
<type 'int'>
<type 'float'>
2.1
<type 'float'>
```

## 文字列型

```python
c = "text" # 「'」「"」のどちらでも可。
d = "テキスト" #Python3ではデフォルトでUnicode文字列として扱われる。
#Python2では「u"テキスト"」と明示する必要あり。

print(c)
print(type(c))
print(d)
print(type(d))
```

```
$ python3 sample_string.py

text
<class 'str'>
テキスト
<class 'str'>
```

## 配列

```python
router_list = ["router_A", "router_B", "router_C"]

# 配列型変数を出力
print(router_list)

# 0から数えて、1番目の値を出力
print(router_list[1])

# 配列の長さを取得(len)
print(len(router_list))
```

```
$ python3 sample_list.py

['router_A', 'router_B', 'router_C']
router_B
3 
```

# 辞書型

```python
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
```

```
$ python3 sample_dictionary.py

{'hostname': 'router_A', 'os': 'junos', 'ip': '192.168.0.1'}
router_A
{'hostname': 'router_A', 'os': 'junos', 'ip': '192.168.0.2'}
```