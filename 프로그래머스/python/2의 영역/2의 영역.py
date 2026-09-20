def solution(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i]==2:
            a.append(i)
    
    if not a:
        return [-1]
    
    return arr[a[0]:a[-1]+1]