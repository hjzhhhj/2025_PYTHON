def gugudan(*numbers):
    for i in numbers:
        for j in range(1, 9+1):
            answer = i * j
            print(f"{i} x {j} = {answer}") 
        print() #줄바꿈
gugudan(2, 3, 7)
