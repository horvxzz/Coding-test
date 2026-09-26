def solution(n):
    a=[]
    b=2
    
    while b<=n:
        if n%b==0:
            a.append(b)
            while n%b==0:
                n//=b
        b+=1
    
    return a