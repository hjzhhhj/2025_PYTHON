import random

def dice_list(sides, count):
    return [random.randint(1, sides) for _ in range(count)]

print(dice_list(6, 5))