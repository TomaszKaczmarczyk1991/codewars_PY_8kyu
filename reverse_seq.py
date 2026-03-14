def reverse_seq(n):
    seq = []

    while n >= 1:
        seq.append(n)
        n -= 1
    return seq

print(reverse_seq(5)) # [5, 4, 3, 2, 1]