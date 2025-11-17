def solution(arr, divisor):
    newlist = []
    for i in arr:
        if i % divisor == 0:
            newlist.append(i)
    if not newlist:
        return [-1]
    return sorted(newlist)