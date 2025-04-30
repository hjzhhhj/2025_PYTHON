jinha_list = [1, 2, 3, 4, 5, 6, 7]

print(jinha_list)
input = int(input("삭제할 값을 입력해주세요! : "))

for i in range (len(jinha_list)):
    if jinha_list[i] == input: 
        jinha_list.pop(i)
        print("삭제한 값의 인덱스는",i,"입니다!")
        break

print(jinha_list)