def solution(myStr):
    a=myStr.replace("a"," ").replace("b"," ").replace("c"," ").split()
    if len(a)==0:
        return ["EMPTY"]
    return a