def solution(s1, s2):
    newlist=set(s1)&set(s2)
    return len(newlist)