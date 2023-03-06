def balloon_pop(y,x):
    pop_range = balloons[y][x]
    amount = 0

    for i in range(-pop_range,pop_range+1):
        if 0 <= y+i < N:
            amount += balloons[y+i][x]
        if 0 <= x+i < M:
            amount += balloons[y][x+i]

    amount -= pop_range

    return amount

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    balloons = [ list(map(int,input().split())) for _ in range(N) ]

    max_amount = 0
    for i in range(N):
        for j in range(M):
            if max_amount < balloon_pop(i,j):
                max_amount = balloon_pop(i,j)

    print(f'#{tc} {max_amount}')

