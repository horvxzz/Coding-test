def solution(my_string,queries):
    a=list(my_string)
    
    for b,c in queries:
        a[b:c+1]=a[b:c+1][::-1]
    
    return ''.join(a)