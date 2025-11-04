def solution(hp):
    g = hp // 5
    hp = hp % 5
    s = hp // 3
    hp = hp % 3
    w = hp
    return g + s + w
