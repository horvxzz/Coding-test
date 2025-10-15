def solution(my_string, n):
    newlist=[]
    for i in my_string:
        newlist.append(i*n)
    return "".join(newlist)