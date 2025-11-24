def solution(a, b):
    s = min(a, b)
    l = max(a, b)
    total = 0
    for i in range(s, l + 1):
        total += i
    return total
