def solution(absolutes, signs):
    x = 0
    a = 0
    for i in absolutes:
        if signs[x] == True:
            a += i
        else:
            a -= i
        x += 1
    return a