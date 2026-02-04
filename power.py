def number_to_pwr(number, p):
    if p == 0:
        return 1
    result = number
    count = 1
    while count < p:
        result *= number
        count += 1
    return result