def solution(numLog):
    y = ''
    for i in range(1, len(numLog)):
        x = numLog[i] - numLog[i-1]
        if x == 1:
            y += 'w'
        elif x == -1:
            y += 's'
        elif x == 10:
            y += 'd'
        elif x == -10:
            y += 'a'
    return y