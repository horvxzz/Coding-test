def solution(spell,dic):
    for i in dic:
        a=sorted(i)
        b=sorted(spell)
        if a==b:
            return 1
    return 2