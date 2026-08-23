def solution(arr, queries):
    for q in queries:
        s=q[0]
        e=q[1]
        k=q[2]
        for i in range(s,e+1):
            if i%k==0:
                arr[i]+=1
    return arr