def solution(x):
    total = 0
    for i in str(x):
        total += int(i)
    return x % total == 0