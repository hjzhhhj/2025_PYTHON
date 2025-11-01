f = open("./파일처리/hangul.txt", "w", encoding="utf-8") 
# 없으면 파일 생성, 있으면 덮어쓰기

f.write("한글")
f.write("\n")
f.write("English")

f.close()

# 한글
# English