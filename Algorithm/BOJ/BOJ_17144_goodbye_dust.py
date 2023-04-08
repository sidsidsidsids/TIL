R, C, T = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(R) ]

'''
T만큼 반복
    미세먼지 확산
    공기청정기 작동
미세먼지 개수 세기
'''

for i in range(R):
    if grid[i][0] == -1:
        act_loc = i
        acb_loc = i+1
        break

def dust():
    diffusion = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] >= 5:
                diffusion.append([i,j,grid[i][j]//5])

    for [y,x,d] in diffusion:
        for ny,nx,nd in [[y-1,x,d],[y,x+1,d],[y+1,x,d],[y,x-1,d]]:
            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] != -1:
                grid[ny][nx] += d
                grid[y][x] -= d

def cleaner():
    # 왼쪽 빗변 (청정기 위)
    if act_loc == 0:
        pass
    else:
        for i in range(act_loc-1,-1,-1):
            if i+1 == act_loc:
                grid[i][0] = 0
            else:
                grid[i][0], grid[i+1][0] = 0, grid[i][0]
    # 왼쪽 빗변 (청정기 아래)
    if acb_loc == R-1:
        pass
    else:
        for i in range(acb_loc+1,R):
            if i-1 == acb_loc:
                grid[i][0] = 0
            else:
                grid[i-1][0], grid[i][0] = grid[i][0], 0
    # 가로 빗변
    for j in range(1,C):
        if grid[0][j-1] == -1:
            grid[0][1] = 0
        else:
            grid[0][j-1], grid[0][j] = grid[0][j], 0
        if grid[R-1][j-1] == -1:
            grid[R-1][1] = 0
        else:
            grid[R-1][j-1], grid[R-1][j] = grid[R-1][j], 0
    # 오른쪽 빗변 (청정기 위)
    for i in range(1,act_loc+1):
        grid[i][C-1], grid[i-1][C-1] = 0, grid[i][C-1]
    # 오른쪽 빗변 (청정기 아래)
    for i in range(R-1, acb_loc-1, -1):
        grid[i-1][C-1], grid[i][C-1] = 0, grid[i-1][C-1]
    # 가운데 (청정기 보통)
    for j in range(C-1,1,-1):
        grid[act_loc][j], grid[act_loc][j-1] = grid[act_loc][j-1], 0
        grid[acb_loc][j], grid[acb_loc][j-1] = grid[acb_loc][j-1], 0

for _ in range(T):
    dust()
    # for a in range(R):
    #     print(grid[a])
    # print()
    cleaner()
    # for a in range(R):
    #     print(grid[a])
    # print()

count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j]:
            count += grid[i][j]

print(count+2)

