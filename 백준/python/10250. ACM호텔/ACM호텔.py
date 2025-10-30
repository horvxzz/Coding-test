t = int(input())  
for _ in range(t):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
        room = N // H
    else:
        room = N // H + 1
    print(f"{floor}{room:02d}")