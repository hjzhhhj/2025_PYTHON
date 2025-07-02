# # # # a = "   Happy Hacking!!   "
# # # # print(len(a))
# # # # # print(a.count("H"))
# # # # # print(a.upper())
# # # # # print(a.lower())
# # # # # print(a.strip())
# # # # # print(a.replace("Happy", "Sad"))
# # # # # print(a.find("ap"))
# # # # # print(a.rfind("a"))
# # # # # print(a.find("앙ㅋㅋ"))

# # # # # print("ap" in a)
# # # # # print("앙ㅋㅋ" in a)

# # # # # b = "hi::hello::whatup?!::hh"
# # # # # print(b.split("::"))

# # # # # c = b.split("::")
# # # # # print(", ".join(c))

# # # # # s = "name: {}, number: {}, age: {}"
# # # # # s.format("hello", 1, 3)
# # # # # print(s)

# # # # # print("{:f}".format(515))
# # # # # print("{:15f}".format(515))
# # # # # print("{:15.2f}".format(515.2583))
# # # # # print("{:=+7.1f}".format(11.17))
# # # # # print("{:=+7.1f}".format(-11.17))

# # # # table = [["월", "화", "수"], ["목", "금", "토"]]
# # # # for row in table:
# # # #     for col in row:
# # # #         print(col, end=" ")

# # # def star(arg, *num):
# # #     for i in range(0, len(num)):
# # #         for j in range(0, num[i]):
# # #             print(arg, end="")
# # #         print()

# # # star("*", 3, 5)

# # # print(f"{x}안녕히하하히ㅏ하{Y}")

# # # Class = hi
# # # mirim07 = hi
# # # mirim__ = hi
# # # mi$rim = hi
# # # MiRiM = hi
# # # mi`rim = hi
# # # m!irim = hi
# # # mir@im = hi
# # # m%irim = hi
# # # m^irim = hi
# # # m&irim = hi
# # # m*irim = hi

# # print(type(6/2))
# # print(type(3**2))
# # print(type(10e4))
# # print(type(4.5*2))
# # print(type(1.2e-3*10))

# a = 9
# a //= 2
# print(a)
# a/=2
# print(a)
# a%=2
# print(a)

# for i in range(1, 6, -1):
#     print(i)
# print()

# for j in [6, 5, 4, 3, 2]:
#     print(j)
# print()

# for a in "65432":
#     print(a)
# print()

# List_a = [2, 3, 4, 5, 6]
# List_a.reverse()
# for b in List_a:
#     print(b)
# print()

# List_b = [1, 2, 7, 3, 8, 4, 9, 5, 10, 6]
# for c in List_b[::-2]:
#     print(c)
# print()

# a = [1, 2, 2, 3, 3, 3]
# a = set(a)
# a = list(a)
# print(a)

# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# tup3 = tup1 + tup2

# print(tup3[2:5])

# tup1[3] = tup2[1]

# for i, v in enumerate(tup3):
#     print(i, v)

# a, b, c = tup1
# print(a, b, c)

# dessert = [
#     {"name" : "candy", "cnt" : 2},
#     {"name" : "jelly", "cnt" : 4},
#     {"name" : "choco", "cnt" : 3}
# ]

# print("가진 디저트 개수")

# for i in dessert:
#     print(i['name'], str(i['cnt'])+"개")

# number = int(input("정수를 입력하시오 : "))
# if number % 2 == 0:
#     print("\n".join(["입력한 수는 {} 입니다.", "{}은/는 짝수입니다."]).format(number, number))
# else:
#     print("\n".join(["입력한 수는 {} 입니다.", "{}은/는 홀수입니다."]).format(number, number))

# a = 3
# if a // 3 > 1:
#     print('a > 5')
# else : 
#     print('a <= 5')

# a = 1
# b = 20.5
# c = '1시 30분'

# print(a+b)
# print(a*b)
# # print(a+c)
# print(a*c)
# print(c*a)
# # print(b*c)
# # print(c/b)

# if 0:
#     print('첫번째 if')
# elif False:
#     print('두번째 if')
# elif '0':
#     print('세번째 if')
# elif 'False':
#     print('마지막 if')

# i = 0
# while 1:
#     print(i, '번째')
#     i += 1
#     if i <= 10:
#         break

# def add(n1, n2 = []):
#     n2.append(n1)
#     sum = 0
#     for i in n2:
#         sum += i
#     return sum

# add(2)
# add(4)
# print(add(6))
# print(add(8))

# L = [1, 2, 3]
# A = [4, 5, 6]
# L.extend(A)
# print(L)

# def multi(*args):
#     num = len(args)
#     print("인자 개수 : ", str(num)+"개")
#     for i in args:
#         print(i, end=" ")

# multi(2, 8, 5, 3)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# def add(n, m):
#     sum = 0
#     for i in range(n, m+1):
#         sum += i
#     return sum

# n = int(input('첫번째 수 : '))
# m = int(input('두번째 수 : '))

# for i in range(n, m+1):
#     if i == m:
#         print(f"{i}=", end="")
#     else:
#         print(f"{i}+", end="")
# print(add(n, m))

# List_star = []
# while(True):
#     a = int(input())
#     if a == 0:
#         break
#     List_star.append(a)

# for i in List_star:
#     for j in range(i + 1):
#         print("*", end="")
#     print()

# def str(x, y, *z):
#     for i in z:
#         print(i)

# def input(a, b, c, d, e):
#     print(a, b, c, d, e)

# def input_2(a, b, c, d, e):
#     print(a, b, c, d, e)

# str(x = 1, y = 2, z = '3', '4', '5')
# input(1, 2, a = 3, b = 4, c = 5)
# input_2(1, 2, c = 3, 4, 5)