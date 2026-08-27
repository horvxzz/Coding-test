def solution(numbers, K):
    a=(K-1)*2
    return numbers[a%len(numbers)]