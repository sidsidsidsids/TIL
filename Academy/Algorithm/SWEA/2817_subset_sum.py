def subset(i,k):
    global cnt

    if i == k:
        if sum(bit) == K:
            cnt += 1
        return
    else:
        bit[i] = numbers[i]
        subset(i+1,k)
        bit[i] = 0
        subset(i+1,k)

t = int(input())
for tc in range(1,1+t):
    N, K = map(int,input().split())
    numbers = list(map(int,input().split()))

    bit = [0] * N
    cnt = 0

    subset(0,N)

    print(f'#{tc} {cnt}')
