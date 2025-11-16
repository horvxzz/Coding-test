def solution(n):
    newlist=[]
    for i in range(n+1):
        if i%2==1:
            newlist.append(i)
    return newlist