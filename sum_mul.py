def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    result = 0
    for num in range(n, m, n):
        result += num
    return result

print(sum_mul(3, 13)) # 30