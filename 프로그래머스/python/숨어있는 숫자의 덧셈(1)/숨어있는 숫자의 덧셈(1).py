def solution(my_string):
    a = 0
    for i in my_string:
        if i.isdigit():
            a += int(i)
    return a