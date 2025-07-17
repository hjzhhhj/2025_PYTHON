import random

initial_money = 50 # 초기 값
goal = 250
wins = 0

for i in range(100): # 라스베가스에 100번 간다.
    cash = initial_money
    while cash > 0 and cash < goal:
        number = random.randint(1, 2)
        if number == 1:
            cash = cash + 1
        else:
            cash = cash - 1
    if cash == goal:
        wins += 1 # $250 이면 카운트

print("초기 금액", initial_money)
print("목표 금액", goal)
print("100번 중에서", wins, "번 성공", sep="")