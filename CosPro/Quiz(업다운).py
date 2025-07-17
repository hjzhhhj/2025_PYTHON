import random

print("1부터 10 사이의 숫자를 맞추시오")
num = random.randint(1, 10)
count = 0

while True:
    count += 1
    ans = int(input("숫자를 입력하시오: "))
    if ans > num:
        print("너무 높음")
    elif ans < num:
        print("너무 낮음")
    else:
        print("축하합니다. 시도횟수=", count)
        break

    