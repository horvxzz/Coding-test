def solution(arr,queries):
    answer=[]

    for s,e,k in queries:
        a=[]
        for i in range(s,e+1):
            if arr[i]>k:
                a.append(arr[i])

        if a:
            answer.append(min(a))
        else:
            answer.append(-1)

    return answer