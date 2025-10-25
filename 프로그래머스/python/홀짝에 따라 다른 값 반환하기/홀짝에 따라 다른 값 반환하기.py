def solution(n):
    if n % 2 == 0:
        a = 0
        for i in range(2, n + 1, 2):
            a += i ** 2
        return a
    else:
        b = 0
        for j in range(1, n + 1, 2):
            b += j
        return b
