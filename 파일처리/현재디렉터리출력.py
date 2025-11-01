import os
data = os.listdir('.')
print(data)

for d in data:
    print(d)
    print("is directory?", os.path.isdir(d))
    print("is file?", os.path.isfile(d))
    
# CosPro
# is directory? True
# is file? False
# 파일처리
# is directory? True
# is file? False
# .DS_Store
# is directory? False
# is file? True ... 