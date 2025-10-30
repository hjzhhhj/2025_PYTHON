def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        str = ( mark * repeat )
        for j in range(2, repeat):
            str = str + (space * space_repeat) + (mark * repeat)
        print(str)