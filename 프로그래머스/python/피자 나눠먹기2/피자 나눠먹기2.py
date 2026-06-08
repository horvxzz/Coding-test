def solution(n):
    a = 1
    while (a * 6) % n != 0:
        a += 1
    return a