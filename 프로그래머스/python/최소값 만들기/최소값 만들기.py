def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    a=0
    for i in range(len(A)):
        a+=A[i]*B[i]
    return a