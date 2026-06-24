def solution(a, d, included):
    b = 0
    for i in range(len(included)):
        if included[i]:
            b += a + d * i
    return b