def solution(t,p):
    a=0
    for b in range(len(t)-len(p)+1):
        if int(t[b:b+len(p)])<=int(p):
            a+=1
    return a