def solution(n):
    newlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            newlist.append(i)
    return newlist
