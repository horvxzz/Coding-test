def solution(rsp):
    result = ""
    for ch in rsp:
        if ch == '2':
            result += '0'
        elif ch == '0':
            result += '5'
        else:
            result += '2'
    return result
