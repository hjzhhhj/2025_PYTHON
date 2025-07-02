def wc(text):
    a = len(text.split())
    b = len(text)
    c = text.count(' ')
    
    return (a, b, c)

print(wc("파이썬 수업"))