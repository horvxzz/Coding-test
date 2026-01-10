def solution(cipher, code):
    a = ""
    for i in range(len(cipher)):
        if (i + 1) % code == 0:
            a += cipher[i]
    return a
