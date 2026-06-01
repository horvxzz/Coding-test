def solution(array, commands):
    b=[]
    for i, j, k in commands:
        a = array[i-1:j]
        a.sort()
        b.append(a[k-1])
    return b