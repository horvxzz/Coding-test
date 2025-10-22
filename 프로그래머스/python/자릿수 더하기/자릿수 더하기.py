def solution(n):
    result = 0
    for i in range(len(str(n))):
        result += n % 10
        n = n // 10
    return result