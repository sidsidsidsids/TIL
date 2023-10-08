def multiplier(n,m):
    if m == 1:
        return n
    else:
        return n * multiplier(n, m-1)


for tc in range(1,11):
    test = int(input())
    N, M = map(int,input().split())
    print(f'#{test} {multiplier(N, M)}')