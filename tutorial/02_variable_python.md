# print

```python
print("Hello World!")
```

```
$ python3 print.py

Hello World!
```

# Variable

Pythonでは、型の指定(「int a;」「float b;」など)は必要なく、自動で型が判定されます。

```python
# 数値型
a = 1
b = 1.1
print(a)
print(b)

c = a + b
print(c)
```

```
$ python3 number.py

1
1.1
2.1
```

```python
# 文字列
c = "text" # 「'」「"」のどちらでも可。
d = "テキスト" #Python3ではデフォルトでUnicode文字列として扱われる。Python2ではu"テキスト"と明示する必要あり。

print(c)
print(d)
```

```
$ python3 string.py

text
テキスト
```


```python
# 配列
list = ['router_A', 'router_B', 'router_C', 'router_D']

# 配列型変数を出力
print(list)

# 0から数えて、2番目の値を出力
print(list[2])

# 配列の長さを取得(len)
print(len(list))
```

```
$ python3 list.py

['router_A', 'router_B', 'router_C', 'router_D']
router_C
4
```

```python
# 辞書型
dictionary = { "hostname" : "router_A", "ip" : "192.168.0.1" } 

print(dictionary)
print(dictionary['hostname'])

# 辞書の一部を、値の代入
dictionary["ip"] = "192.168.0.2"

print(dictionary)
```

```
$ python3 dictionary.py

# print(dictionary) の実行結果
{'hostname': 'router_A', 'ip': '192.168.0.1'}

# print(dictionaryp['hostname']) の実行結果
router_A

# 値を代入したあとの、print(dictionary)の実行結果
{'hostname': 'router_A', 'ip': '192.168.0.2'}
```