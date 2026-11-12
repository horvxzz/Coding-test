def solution(arr):
    a=len(arr)
    b=len(arr[0])

    if a>b:
        for i in range(a):
            arr[i]+=[0]*(a-b)
    elif a<b:
        for i in range(b-a):
            arr.append([0]*b)

    return arr