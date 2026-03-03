def solution(left, right):
    total = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) ** 2 == i:
            total -= i
        else:
            total += i
    return total