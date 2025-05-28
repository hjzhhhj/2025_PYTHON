import random

def dice_list(sides, count):
    answer = []  
    for i in range(count): 
        a = random.randint(1, sides) 
        answer.append(a)  
    return answer

print(dice_list(6, 5))