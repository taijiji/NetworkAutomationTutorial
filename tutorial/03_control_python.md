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
$ python3 if.py

num is two
```

# for

```python
for num in range(5):
    print(num)

list = ['router_A', 'router_B', 'router_C', 'router_D']
for name in list:
    print(name)
```

```
$ python3 for.py

0
1
2
3
4
router_A
router_B
router_C
router_D
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
$ python3 function.py

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
$ python3 class.py

Router A
```

# open file
