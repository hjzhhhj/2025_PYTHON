now = int(input("현재 몸무게 : "))
will = int(input("목표 몸무게 : "))

week = 1

while now > will:
    now -= int(input(f"{week}주차 감량 몸무게 : "))
    week += 1

print(now, "kg 달성! 축하합니다!")
