def solution(emergency):
    a=sorted(emergency, reverse=True)
    b=[]
    for i in emergency:
        b.append(a.index(i)+1)
    return b