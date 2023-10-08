N, M = map(int,input().split())
start_i, start_j, direction = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

rdi = [1, 0, -1, 0]
rdj = [0, -1, 0, 1]

def cleaner(y,x,d):
    clean = 0
    switch = True
    while switch == True:
        if grid[y][x] == 0:
            grid[y][x] = -1
            clean += 1
        elif grid[y][x] != 0:
            cnt = 0
            for ni, nj in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
                if 0 <= ni < N and 0 <= nj < M:
                    if grid[ni][nj] == 0:
                        cnt += 1
                        break
            if cnt == 0: # 청소되지 않은 빈 칸이 없는 경우
                if grid[y+rdi[d]][x+rdj[d]] == 1:
                    switch = False
                    break
                else:
                    y += rdi[d]
                    x += rdj[d]
            else:
                d -= 1
                if d == -1:
                    d = 3
                elif d == 4:
                    d = 0
                if grid[y+di[d]][x+dj[d]] == 0:
                    y += di[d]
                    x += dj[d]
    return clean

print(cleaner(start_i,start_j,direction))