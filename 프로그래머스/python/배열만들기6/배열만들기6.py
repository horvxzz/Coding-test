def solution(arr):
    a=[]
    i=0
    
    while i<len(arr):
        if not a:
            a.append(arr[i])
        elif a[-1]==arr[i]:
            a.pop()
        else:
            a.append(arr[i])
        i+=1
    
    if not a:
        return [-1]
    return a