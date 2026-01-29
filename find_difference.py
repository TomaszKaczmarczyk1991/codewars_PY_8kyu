def find_difference(a, b):
    vol1 = 1
    vol2 = 1

    for x in a:
        vol1 *= x

    for x in b:
        vol2 *= x
        
    return abs(vol1 - vol2)