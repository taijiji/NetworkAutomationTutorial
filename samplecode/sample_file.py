# 読み込みモード:"r"
file1 = open("sample_read.txt", "r")
text = file1.read() # ファイル全文を文字列として読み込み
#text = file1.readline() # ファイル1行目のみを文字列として読み込み
#text = file1.readlines() # ファイルを行ごとに配列として読み込み
print(text)
file1.close()

# 上級者向け
# with open("sample_read.txt", "r") as file:
#  whole_str = file.read()


# 上書き書き込みモード:"w", 追記書き込みモード:"a"
file2 = open("sample_write.txt", "w") 
file2.write("Good!")
file2.close()