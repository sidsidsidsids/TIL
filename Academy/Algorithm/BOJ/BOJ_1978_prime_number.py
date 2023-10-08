N = int(input())
numbers = list(map(int,input().split()))
cnt = 0

for n in numbers:
    check = []
    for t in range(1,n+1):
        if not n % t:
            check.append(t)
    if len(check) == 2:
        cnt += 1

print(cnt)