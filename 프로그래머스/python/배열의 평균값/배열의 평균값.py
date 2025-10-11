def solution(numbers):
    n=0
    s=0
    m=0
    for i in numbers:
        n+=i
        s+=1
    m=n/s
    return m