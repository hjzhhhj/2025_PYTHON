def sum(numbers):
    total = 0
    for i in range(len(numbers)):       # 행 카운트
        for j in range(len(numbers[0])): # 열 카운트
            total = total + numbers[i][j]
    return total

data = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
rows = len(data)
cols = len(data[0])

# 데이터 출력
for r in range(rows):  # 행 카운트
    print(r, '행 :', end=" ")
    for c in range(cols):  # 열 카운트
        print(data[r][c], end=" ")
    print()

# total = sum(sum(row) for row in data)
# print('데이터 합 =', total)
print('데이터 합 =', sum(data))
