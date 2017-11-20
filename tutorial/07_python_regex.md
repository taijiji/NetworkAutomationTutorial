# Regular Expresion

```python
import re

# 複数行の文字列
# show versionコマンド実行結果を想定
show_version_txt = """
Hostname: vsrx
Model: firefly-perimeter
JUNOS Software Release 12.1X47-D15.4
"""

# 正規表現
# 「()」: グループ化
# 「.」 : 改行以外の任意の文字列1文字
# 「+」 : 直前の正規表現に対して、１回以上の繰り返し
regex = "JUNOS Software Release (.+)"

# show_version_txtの文字列に対して、正規表現による文字列の抽出を実行
match = re.search(regex, show_version_txt )

# マッチした文字文字列全体を表示
print(match.group(0))
# マッチした文字列のうちグループ化された部分を抽出
print(match.group(1))
```

```
$ python3 sample_regex.py

JUNOS Software Release 12.1X47-D15.4
12.1X47-D15.4
```

https://docs.python.org/ja/3/library/re.html
https://docs.python.jp/3/howto/regex.html
