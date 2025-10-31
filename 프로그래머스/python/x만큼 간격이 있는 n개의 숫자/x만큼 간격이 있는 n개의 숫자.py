def solution(x, n):
    newlist = []
    for i in range(1, n+1):
        newlist.append(x * i)
    return newlist