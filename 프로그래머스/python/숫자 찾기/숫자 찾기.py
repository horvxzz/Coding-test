def solution(num, k):
    a=str(num).find(str(k))
    if a != -1:
        return a+1
    else:
        return -1