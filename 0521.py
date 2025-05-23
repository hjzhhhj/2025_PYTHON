def star(args, *num):
    result = 1
    for n in num:
        result *= n
    print(args * result)

star("*", 3)           # 출력: ***
star("*", 1, 2, 3)      # 출력: ******