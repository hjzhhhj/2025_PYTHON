user = input("정수를 입력하시오 : ").split(" ")
print("입력한 정수 리스트 : ", user)
zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

for i in user:
    num = (int(i)) % 10
    if num == 0: zero+=1
    elif num == 1: one+=1
    elif num == 2: two+=1
    elif num == 3: three+=1
    elif num == 4: four+=1
    elif num == 5: five+=1
    elif num == 6: six+=1
    elif num == 7: seven+=1
    elif num == 8: eight+=1
    elif num == 9: nine+=1

if zero > 0: print(f"0 : {zero}개")
if one > 0: print(f"1 : {one}개")
if two > 0: print(f"2 : {two}개")
if three > 0: print(f"3 : {three}개")
if four > 0: print(f"4 : {four}개")
if five > 0: print(f"5 : {five}개")
if six > 0: print(f"6 : {six}개")
if seven > 0: print(f"7 : {seven}개")
if eight > 0: print(f"8 : {eight}개")
if nine > 0: print(f"9 : {nine}개")

