def solution(intStrs,k,s,l):
    a=[]
    
    for b in intStrs:
        c=int(b[s:s+l])
        if c>k:
            a.append(c)
    
    return a