def solution(a):
    for i in range(len(a)):
        if a[i] >= 50 and a[i] % 2 == 0:
            a[i] //= 2
        elif a[i] < 50 and a[i] % 2 != 0:
            a[i] *= 2
    return a