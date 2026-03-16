def solution(arr, k):
    newlist=[]
    a=0
    if k%2==0:
        for i in arr:
            a=i+k
            newlist.append(a)
    else:
        for i in arr:
            a=i*k
            newlist.append(a)
    return newlist
            
            