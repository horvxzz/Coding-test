def solution(n, numlist):
    newlist=[]
    for i in numlist:
        if i%n==0:
            newlist.append(i)
    return newlist
        