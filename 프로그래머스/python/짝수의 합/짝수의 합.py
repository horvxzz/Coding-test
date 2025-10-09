def solution(n):
    sums=0
    for i in range(n+1):
        if i%2==0:
            sums+=i
    return sums