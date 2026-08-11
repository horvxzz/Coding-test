def solution(my_string):
    a=""
    b=0
    
    for i in my_string:
        if i.isdigit():
            a+=i
        else:
            if a:
                b+=int(a)
                a=""
                
    if a:
        b+=int(a)
        
    return b