def solution(arr):
    newlist = []
    for i in arr:
        if not newlist or newlist[-1] != i:
            newlist.append(i)
    return newlist