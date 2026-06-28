def solution(array):
    a = 0
    for i in array:
        a += str(i).count('7')
    return a