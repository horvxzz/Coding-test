def solution(picture,k):
    a=[]
    for b in picture:
        c=""
        for d in b:
            c+=d*k
        for i in range(k):
            a.append(c)
    return a