def solution(arr):
    a=0
    
    while True:
        b=[]
        for c in arr:
            if c>=50 and c%2==0:
                b.append(c//2)
            elif c<50 and c%2==1:
                b.append(c*2+1)
            else:
                b.append(c)
        
        if arr==b:
            return a
        
        arr=b
        a+=1