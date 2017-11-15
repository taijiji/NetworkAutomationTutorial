c = "text" # 「'」「"」のどちらでも可。
d = "テキスト" #Python3ではデフォルトでUnicode文字列として扱われる。
#Python2では「u"テキスト"」と明示する必要あり。

print(c)
print(type(c))
print(d)
print(type(d))