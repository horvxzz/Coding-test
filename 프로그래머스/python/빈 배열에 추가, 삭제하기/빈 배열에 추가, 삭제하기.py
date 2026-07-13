def solution(arr, flag):
    a=[]
    for i in range(len(arr)):
        if flag[i]:
            for j in range(arr[i]*2):
                a.append(arr[i])
        else:
            for j in range(arr[i]):
                a.pop()
    return a