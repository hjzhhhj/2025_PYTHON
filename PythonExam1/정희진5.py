floor = int(input("층 수 : "))
print(f"{floor}층 숫자 피라미드:\n")

for i in range(1, floor + 1):
    num = 1
    line = []
    for j in range(1, i + 1):
        line.append(str(num))
        num += j + 1  # 다음 숫자는 이전 숫자 + 다음 줄 번호

    # 출력 (오른쪽 정렬)
    print(" " * (floor - i) * 2 + " ".join(line))

