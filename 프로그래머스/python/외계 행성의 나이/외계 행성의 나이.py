def solution(age):
    return ''.join(chr(int(n) + 97) for n in str(age))