list = [1, 2, 3, 4, 5, 6, 7]
value = int(input("삭제할 값을 입력하세요: "))

found = False
for i in range(len(list)):
    if list[i] == value:
        print("삭제한 값의 인덱스:", i)
        del list[i]
        found = True
        break

if not found:
    print("해당 값이 리스트에 없습니다.")
else:
    print("삭제 후 리스트:", lst)
