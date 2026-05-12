def solution(arr):
    a = []
    for i in arr:
        for j in range(i):
            a.append(i)
    return a