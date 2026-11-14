def solution(rank,attendance):
    a=[]
    for i in range(len(rank)):
        if attendance[i]:
            a.append([rank[i],i])
    a.sort()
    b=a[0][1]
    c=a[1][1]
    d=a[2][1]
    return 10000*b+100*c+d