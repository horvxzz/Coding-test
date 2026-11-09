def solution(s):
    a=s.split()
    b=[]
    for i in a:
        if i=="Z":
            b.pop()
        else:
            b.append(int(i))
    return sum(b)