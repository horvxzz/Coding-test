def solution(i, j, k):
    a=""
    for n in range(i,j+1):
        a+=str(n)
    return a.count(str(k))