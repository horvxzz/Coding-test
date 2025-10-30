def time(x,y):
  if y >= 45:
    return x, y - 45
  else:
    n = x - 1
    if n < 0:
        n = 23
    m = y + 15  
    return n, m
i,j=map(int, input().split())
x,y=time(i,j)
print(x,y)