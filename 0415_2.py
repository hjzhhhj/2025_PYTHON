for i in range(7):
    s = i+1 if i < 4 else 7-i
    print('*'*s + ' '*(7-s*2) + '*'*s if s*2 < 7 else '*'*7)
