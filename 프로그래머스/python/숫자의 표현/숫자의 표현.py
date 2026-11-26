def solution(n):
    a=0
    for i in range(1,n+1):
        b=0
        for j in range(i,n+1):
            b+=j
            if b==n:
                a+=1
                break
            elif b>n:
                break
    return a