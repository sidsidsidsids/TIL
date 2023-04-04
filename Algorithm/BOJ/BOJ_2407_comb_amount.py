n, m = map(int,input().split())
target = n/m
for _ in range(m-1):
    n -= 1
    target *= n
for _ in range(m-1):
    m -= 1
    target //= m
print(int(target))
