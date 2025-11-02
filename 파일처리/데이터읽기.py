f = open("./파일처리/text.txt", "w", encoding="utf-8")
# 없으면 파일 생성, 있으면 덮어쓰기

f.write("안녕하세요")
f.write("\n")
f.write("반갑습니다")

f.close()

f = open("./파일처리/text.txt", "r", encoding="utf-8")
# 없으면 오류 발생, 있으면 읽기

print(f.read())

f.close()