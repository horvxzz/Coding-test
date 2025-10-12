def solution(sides):
    n=max(sides)
    sides.remove(n)
    s=0
    for i in sides:
        s+=i
    if s>n:
        return 1
    else:
        return 2