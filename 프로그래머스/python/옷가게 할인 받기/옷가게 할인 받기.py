def solution(price):
    if price >= 500000:
        discount = 0.20
    elif price >= 300000:
        discount = 0.10
    elif price >= 100000:
        discount = 0.05
    else:
        discount = 0

    return int(price * (1 - discount))
