N, L = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

cnt = 0

def checking(grid_way):
    way = [0] * N
    for i in range(N):
        way[i] += grid_way[i]

    check_loc = 0

    able = True

    while check_loc < N-1:
        if way[check_loc] == way[check_loc+1]:
            check_loc += 1
        else:
            if abs(way[check_loc] - way[check_loc+1]) > 1:
                able = False
                break
            else:
                if way[check_loc] < way[check_loc+1]:
                    if L == 1:
                        check_loc += 1
                    else:
                        if check_loc - (L-1) >= 0:
                            if sum(way[check_loc-(L-1):check_loc+1]) % L == 0:
                                for i in range(1,L):
                                    way[check_loc-(i-1)] += 1
                                check_loc += 1
                            else:
                                able = False
                                break
                        else:
                            able = False
                            break
                else: # way[check_loc] > way[check_loc+1]:
                    if check_loc + L <= N:
                        if sum(way[check_loc+1:check_loc+(L+1)]) % L == 0:
                            for i in range(1,L):
                                way[check_loc+i] += 1
                            check_loc += 1
                        else:
                            able = False
                            break
                    else:
                        able = False
                        break

    if able:
        print(grid_way)
        return 1
    else:
        return 0

# 가로
for i in range(N):
    cnt += checking(grid[i])

# 세로
sero_way = [0] * N
for j in range(N):
    for i in range(N):
        sero_way[i] = grid[i][j]
    cnt += checking(sero_way)

print(cnt)



