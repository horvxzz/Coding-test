def solution(myString, pat):
    a=0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)]==pat:
            a+=1
    return a