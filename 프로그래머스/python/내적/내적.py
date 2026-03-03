def solution(a, b):
    n=0
    for i in range(len(a)):
        n+=a[i]*b[i]
    return n