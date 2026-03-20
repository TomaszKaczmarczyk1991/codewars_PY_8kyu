import math

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)