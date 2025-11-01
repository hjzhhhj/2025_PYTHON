f = open("./파일처리/file.txt", "w")

f.write("Hello")
f.write("\n")
f.write("World")

f.close()

f = open("./파일처리/file.txt", "a")

f.write("\n")
f.write("append")

f.close()