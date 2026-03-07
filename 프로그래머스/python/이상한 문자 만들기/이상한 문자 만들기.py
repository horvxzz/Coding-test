def solution(s):
    newstr = ''
    idx = 0
    for i in s:
        if i == ' ':
            newstr += ' '
            idx = 0
        else:
            if idx % 2 == 0:
                newstr += i.upper()
            else:
                newstr += i.lower()
            idx += 1
    return newstr