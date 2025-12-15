def powers_of_two(n):
    count = 0
    result = []
    while count <= n:
        result.append(2**count)
        count += 1
    return result

print(powers_of_two(4)) // [1, 2, 4, 8, 16]