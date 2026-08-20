def solution(order):
    a=0
    for i in order:
        if "cafelatte" in i:
            a+=5000
        else:
            a+=4500
    return a