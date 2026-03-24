def solution(str_list, ex):
    newstr = ''
    for i in str_list:
        if ex not in i:
            newstr += i
    return newstr