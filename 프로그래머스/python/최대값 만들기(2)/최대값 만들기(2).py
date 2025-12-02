def solution(numbers):
    numbers.sort()
    b = numbers[-1] * numbers[-2]
    s = numbers[0] * numbers[1]
    
    return max(b, s)
