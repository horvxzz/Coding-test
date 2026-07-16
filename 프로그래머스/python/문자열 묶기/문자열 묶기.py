def solution(strArr):
    a={}
    for i in strArr:
        b=len(i)
        if b in a:
            a[b]+=1
        else:
            a[b]=1
    return max(a.values())