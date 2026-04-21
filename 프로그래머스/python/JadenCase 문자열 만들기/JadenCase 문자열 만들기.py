def solution(s):
    a = []
    words = s.split(' ')
    for i in words:
        a.append(i.capitalize())
    return " ".join(a)