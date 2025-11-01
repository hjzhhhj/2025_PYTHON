n = 7

for i in range(n, 0, -2):
    space = (n - i) // 2
    print("  " * space + "* " * i)

for i in range(3, n + 1, 2):
    space = (n - i) // 2
    print("  " * space + "* " * i)
