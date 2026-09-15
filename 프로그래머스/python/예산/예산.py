def solution(d,budget):
    d.sort()
    a=0
    b=0
    
    for c in d:
        if b+c<=budget:
            b+=c
            a+=1
        else:
            break
    
    return a