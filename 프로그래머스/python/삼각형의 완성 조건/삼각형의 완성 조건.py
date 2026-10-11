def solution(sides):
    a=min(sides)
    b=max(sides)
    c=0
    
    for d in range(b-a+1,b+a):
        c+=1
    
    return c