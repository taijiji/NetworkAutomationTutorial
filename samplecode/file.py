file1 = open("sample_read.txt", "r")
text = file1.read() # ファイル全文を文字列として読み込み
#text = file1.readline() # ファイル1行目のみを文字列として読み込み
#text = file1.readlines() # ファイルを行ごとに配列として読み込み
print(text)

file2 = open("sample_write.txt", "w")
file2.write("Good!")
file2.close