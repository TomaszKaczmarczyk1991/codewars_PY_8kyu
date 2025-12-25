def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0
    arr.sort(reverse=True)

    total = 0
    for i in range(len(arr) - 1):
        total += arr[i] - arr[i + 1]

    return total

print(sum_of_differences([2,1,10])) # 9
