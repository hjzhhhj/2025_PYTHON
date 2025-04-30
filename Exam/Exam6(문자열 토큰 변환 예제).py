a = input()

if a.startswith("print("):
    text = a[6:-2]
    print(text[1:-1], end="")
elif a.startswith("println("):
    text = a[8:-2]
    print(text[1:-1])
else:
    print("오류가 발생했습니다!")
