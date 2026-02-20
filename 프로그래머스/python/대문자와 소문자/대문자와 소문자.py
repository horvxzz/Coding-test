def solution(my_string):
    newlist = ""
    for i in my_string:
        if i.isupper():
            newlist += i.lower()
        else:
            newlist += i.upper()
    return newlist