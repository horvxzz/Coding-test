def solution(quiz):
    a=[]
    for b in quiz:
        c=b.split()
        d=int(c[0])
        e=int(c[2])
        f=int(c[4])
        
        if c[1]=="+":
            g=d+e
        else:
            g=d-e
        
        if g==f:
            a.append("O")
        else:
            a.append("X")
    return a