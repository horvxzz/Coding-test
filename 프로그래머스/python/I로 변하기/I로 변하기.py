def solution(myString):
    str1 = ""
    for i in myString:
        if i < "l":
            str1 += "l"
        else:
            str1 += i
    return str1