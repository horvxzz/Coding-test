def solution(myString, pat):
    newstr = ''
    for i in myString:
        if i == 'A':
            newstr += 'B'
        else:
            newstr += 'A'
    if pat in newstr:
        return 1
    else:
        return 0