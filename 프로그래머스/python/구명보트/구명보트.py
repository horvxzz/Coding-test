def solution(people,limit):
    people.sort()
    a=0
    b=len(people)-1
    c=0
    while a<=b:
        if people[a]+people[b]<=limit:
            a+=1
        b-=1
        c+=1
    return c