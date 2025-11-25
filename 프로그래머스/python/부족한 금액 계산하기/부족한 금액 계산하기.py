def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += price * i

    return max(total - money, 0)
