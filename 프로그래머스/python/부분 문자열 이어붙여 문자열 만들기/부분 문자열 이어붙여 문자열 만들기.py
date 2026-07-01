def solution(my_strings, parts):
    a = ""
    for i in range(len(my_strings)):
        s = parts[i][0]
        e = parts[i][1]
        a += my_strings[i][s:e+1]
    return a