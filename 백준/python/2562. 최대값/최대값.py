m = 0
i = 0

for x in range(9):
    n = int(input())
    if n > m:
        m = n
        i = x + 1

print(m)
print(i)