def solution(balls,share):
    a=1
    b=1

    for i in range(share):
        a*=balls-i
        b*=i+1

    return a//b