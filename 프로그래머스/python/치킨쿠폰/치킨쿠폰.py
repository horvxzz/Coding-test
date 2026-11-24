def solution(chicken):
    a=0
    while chicken>=10:
        b=chicken//10
        a+=b
        chicken=chicken%10+b
    return a