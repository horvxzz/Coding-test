def solution(my_str, n):
    a=[]
    for i in range(0,len(my_str),n):
        a.append(my_str[i:i+n])
    return a