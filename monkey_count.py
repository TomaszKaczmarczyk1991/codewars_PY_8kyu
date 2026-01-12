def monkey_count(n):
    arr = []
    r = range(1,n + 1,1)
    for x in r:
        arr.append(x)
    return arr

print(monkey_count(5)) # [1, 2, 3, 4, 5]