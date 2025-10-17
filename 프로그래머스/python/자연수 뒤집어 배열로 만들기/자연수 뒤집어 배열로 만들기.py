def solution(n):
    newlist=[]
    while True:
        if n==0:
            break
        newlist.append(n%10)
        n=n//10
    return newlist
