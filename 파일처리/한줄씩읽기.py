f = open("./파일처리/text.txt", "r", encoding="utf-8")

line1 = f.readline()
print("line1 : ", line1)
line2 = f.readline()
print("line2 : ", line2)
line3 = f.readline()
print("line3 : ", line3)

f.close()

# line1 :  안녕하세요
# line2 :  반갑습니다
# line3 :  
