# PIP
Python Package Index

# Check PIP version

```
$ pip --version

pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages (python 2.7)
```

```
$ pip2 --version

pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages (python 2.7)
```

```
$ pip3 --version

pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (python 3.6)
```

# Check list of exsiting package

```
$ pip3 list

Jinja2 (2.9.6)
numpy (1.13.1)
PyYAML (3.12)
```

# Install new package

```
$ pip3 install jinja2
```

# Using Python Library

```python
# datetime ライブラリのインポート
import datetime

# datetimeライブラリの、datetimeクラスのnow関数を実施。
now = datetime.datetime.now()
print(now)
```

```
$ python3 sample_library.py

2017-11-15 14:25:56.360603
```

