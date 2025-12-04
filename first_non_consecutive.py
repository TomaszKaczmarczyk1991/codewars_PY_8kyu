def first_non_consecutive(arr):
    prev = arr[0]
    for x in arr[1:]:
        if x != prev + 1:
            return x
        prev = x