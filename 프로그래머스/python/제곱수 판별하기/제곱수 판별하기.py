def solution(n):
    s=n**0.5
    if s.is_integer():
        return 1
    else:
        return 2