def solution(name,yearning,photo):
    a={}
    for i in range(len(name)):
        a[name[i]]=yearning[i]
    b=[]
    for c in photo:
        d=0
        for e in c:
            d+=a.get(e,0)
        b.append(d)
    return b