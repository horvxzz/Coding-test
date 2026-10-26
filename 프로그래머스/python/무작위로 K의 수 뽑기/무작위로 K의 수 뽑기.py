def solution(arr,k):
    a=[]

    for b in arr:
        if b not in a:
            a.append(b)
        if len(a)==k:
            break

    while len(a)<k:
        a.append(-1)

    return a