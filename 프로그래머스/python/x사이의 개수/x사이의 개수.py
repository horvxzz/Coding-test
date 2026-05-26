def solution(myString):
    split_list = myString.split('x')
    a = []
    for s in split_list:
        a.append(len(s))
    return a