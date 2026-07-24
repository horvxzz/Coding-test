def solution(array, n):
    array.sort()
    a=array[0]
    for i in array:
        if abs(n-i)<abs(n-a):
            a=i
    return a