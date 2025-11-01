f = open("./파일처리/file.txt", "w")

f.write("Hello")
f.write("\n")
f.write("World")

f.close()

# Hello
# World

# open mode: w, r, a, rb, wb
# w: write, r: read, a: append, rb: read binary, wb: write binary
