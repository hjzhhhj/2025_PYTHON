length = int(input("입력할 이메일의 개수를 입력해주세요! : "))
email_list = []

for i in range(length):
    a = input("이메일을 입력해주세요! : ")

    if "@" in a and "." in a:
        if not a.startswith("@") and not a.startswith("."):
            if a.find("@") != -1 and "." in a[a.find("@"):]:
                email_list.append(a)
                print(a, "가 리스트에 추가되었습니다!")
            else:
                print("오류 발생 : @ 뒤에 .이 없어요.")
        else:
            print("오류 발생 : 시작이 @이거나 .이면 안돼요.")
    else:
        print("오류 발생 : 이메일 안에 @와 .이 포함되어야 해요.")
