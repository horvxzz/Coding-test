def solution(s):
    a=[]
    for i in s:
        if s.count(i)==1:
            a.append(i)
    return ''.join(sorted(a))