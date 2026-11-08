def solution(keyinput,board):
    x=0
    y=0
    a=board[0]//2
    b=board[1]//2

    for i in keyinput:
        if i=="up" and y<b:
            y+=1
        elif i=="down" and y>-b:
            y-=1
        elif i=="left" and x>-a:
            x-=1
        elif i=="right" and x<a:
            x+=1

    return [x,y]