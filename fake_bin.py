def fake_bin(x):
    binary = []
    for num in x:
        if int(num) < 5:
            binary.append('0')
        else:
            binary.append('1')
    return "".join(binary)

print(fake_bin("45385593107843568")) # 01011110001100111