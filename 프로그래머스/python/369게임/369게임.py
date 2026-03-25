def solution(order):
    a = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            a += 1
    return a