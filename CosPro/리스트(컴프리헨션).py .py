# 1~19 숫자 중에서 3의 배수로만 리스트를 구성하는 다양한 예제
data = [num for num in range(1, 20) if num % 3 == 0]

print(data)

for index, value in enumerate(data):
    print('(', index, ':', value, ')', end=' ')
print()

for i in range(len(data)):
    print(data[i], end=' ')
print()

for i in data:
    print(i, end=' ')
print()
