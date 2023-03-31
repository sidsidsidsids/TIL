def subset_sum(i,k,v):
    global ans
    if v - H > ans and i < k:
        return
    if i == k:
        if sum(bit) >= H:
            val = sum(bit) - H
            if val < ans:
                ans = val
    else:
        bit[i] = numbers[i]
        v += bit[i]
        subset_sum(i+1,k,v)
        v -= bit[i]
        bit[i] = 0
        subset_sum(i+1,k,v)

t = int(input())
for tc in range(1,1+t):
    N, H = map(int,input().split())
    numbers = list(map(int,input().split()))

    bit = [0] * N
    ans = 0
    ans += H

    subset_sum(0,N,0)

    print(f'#{tc} {ans}')