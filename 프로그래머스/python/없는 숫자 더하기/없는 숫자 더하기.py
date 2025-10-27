def solution(numbers):
    a=0
    for i in range(10):
        if i not in numbers:
            a+=i
    return a