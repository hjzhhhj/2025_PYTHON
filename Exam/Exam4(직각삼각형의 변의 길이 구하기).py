for a in range(1, 400):
    for b in range(a+1, 400):  # b는 a보다 커야 하므로 a+1부터
        c = 400 - a - b 
        if a**2 + b**2 == c**2:  
            print(a, b, c)  
            break
