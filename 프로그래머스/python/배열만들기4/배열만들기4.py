def solution(arr):
    a=[]
    i=0
    
    while i<len(arr):
        if not a:
            a.append(arr[i])
            i+=1
        elif a[-1]<arr[i]:
            a.append(arr[i])
            i+=1
        else:
            a.pop()
    
    return a