N, K = map(int,input().split())

money = [0] * N
for i in range(N):
    price = int(input())
    money[i] = price
cnt = 0
while K:
    if K >= money[-1]:
        cnt += K//money[-1]
        K -= money[-1] * (K//money[-1])
    else:
        for i in range(N-1):
            if money[i] <= K < money[i+1]:
                K -= money[i]
                cnt += 1
print(cnt)

