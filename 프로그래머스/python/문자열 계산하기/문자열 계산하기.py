def solution(my_string):
    a=my_string.split()
    b=int(a[0])

    for i in range(1,len(a),2):
        if a[i]=="+":
            b+=int(a[i+1])
        else:
            b-=int(a[i+1])

    return b