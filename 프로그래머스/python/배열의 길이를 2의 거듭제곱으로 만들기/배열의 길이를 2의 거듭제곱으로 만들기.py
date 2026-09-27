def solution(arr):
    a=1
    while a<len(arr):
        a*=2
    
    return arr+[0]*(a-len(arr))