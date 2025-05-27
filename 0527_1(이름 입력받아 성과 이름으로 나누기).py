def div_name(name):
    a = name.strip().split()
    if len(a) >= 2:
        return a[0], ' '.join(a[1:])
    else:
        return a[0], ''
    
name1, name2 = div_name("김이박최정 희진")
print("성:", name1)
print("이름:", name2)
