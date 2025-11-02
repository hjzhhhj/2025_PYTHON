import array
f = open("./파일처리/data.bin", "wb")

byte_arr = []
for i in range(0, 256):
    byte_arr.append(i)
    
data = bytes(byte_arr)
f.write(data)

f.close()

f = open("./파일처리/data.bin", "rb")

data = array.array('B')
data.fromfile(f, 10)

for item in data:
    print(item, end=' ')
    
f.close()