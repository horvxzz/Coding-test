def solution(array):
    a={}
    for i in array:
        a[i]=a.get(i,0)+1
    b=max(a.values())
    c=[i for i in a if a[i]==b]
    if len(c)>1:
        return -1
    return c[0]