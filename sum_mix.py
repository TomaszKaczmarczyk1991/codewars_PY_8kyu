# def sum_mix(arr):
#     result = 0
#     for num in arr:
#         result += int(num)
#     return result


def sum_mix(arr):
    return sum(int(num) for num in arr)