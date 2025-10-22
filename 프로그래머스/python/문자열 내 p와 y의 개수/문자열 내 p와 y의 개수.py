def solution(s):
    s=s.lower()
    a=s.count('y')
    b=s.count('p')
    if a==b:
        return True
    elif a!=b:
        return False
    else:
        return True