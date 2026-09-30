def solution(my_string):
    a=[0]*52
    
    for b in my_string:
        if b.isupper():
            a[ord(b)-ord('A')]+=1
        else:
            a[ord(b)-ord('a')+26]+=1
    
    return a