import random

def dice_game():
    while True:
        x = random.randint(1, 6)
        y = random.randint(1, 6)

        print("인간: 주사위값 = ", x)
        print("컴퓨터: 주사위값 = ", y)

        if x > y:
            print("인간승리")
        elif x < y:
            print("컴퓨터승리")
        else:
            print("비김")

        ans = input("중단할까요? y/n >> ").lower()
        if ans == "y":
            break
        elif ans == "n":
            continue

dice_game()