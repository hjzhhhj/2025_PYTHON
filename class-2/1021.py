f = open("data.bin", "wb")
byte_arr = bytes([255, 0, 127])
f.write(byte_arr)
f.close()