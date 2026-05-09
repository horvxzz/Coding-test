def solution(number):
    a = 0
    for i in number:
        a += int(i)
    return a % 9