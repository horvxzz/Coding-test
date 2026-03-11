def solution(a, b, c):
    n = [a, b, c]
    if len(set(n)) == 3:
        return a+b+c
    elif len(set(n)) == 2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)