def solution(my_string, s, e):
    a=list(my_string)
    b=a[s:e+1]
    b.reverse()
    a[s:e+1]=b
    return ''.join(a)