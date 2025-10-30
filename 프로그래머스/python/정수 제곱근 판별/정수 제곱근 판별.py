def solution(n):
    s = n ** 0.5
    if s.is_integer():
        return int((s + 1) ** 2)
    else:
        return -1
