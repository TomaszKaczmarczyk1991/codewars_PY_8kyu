def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

print(count_by(2, 5)) # [2, 4, 6, 8, 10]