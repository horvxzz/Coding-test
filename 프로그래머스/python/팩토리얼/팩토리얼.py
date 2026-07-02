def solution(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        if a > n:
            return i - 1
    return n