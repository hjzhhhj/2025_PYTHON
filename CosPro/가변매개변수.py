def sum_many(*var):
    sum = 0
    for i in var:
        sum = sum + i

    print("모든 값을 더하면: ", sum)

sum_many(1, 2, 3)
sum_many(1, 2, 3, 4, 5, 6)
sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)