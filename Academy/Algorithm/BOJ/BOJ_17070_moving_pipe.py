n = int(input())
grid = [ list(map(int,input().split())) for _ in range(n) ]

cnt = 0

def moving_pipe(i,j,idx):
    global cnt
    if i == n-1 and j == n-1:
        cnt += 1
        return

    if idx == 0:
        if j+1 < n and grid[i][j+1] == 0:
            moving_pipe(i,j+1,0)
        if j+1 < n and i+1 < n and grid[i+1][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j+1] == 0:
            moving_pipe(i+1,j+1,1)
    elif idx == 1:
        if j+1 < n and grid[i][j+1] == 0:
            moving_pipe(i,j+1,0)
        if i + 1 < n and grid[i + 1][j] == 0:
            moving_pipe(i + 1, j, 2)
        if j + 1 < n and i + 1 < n and grid[i + 1][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j + 1] == 0:
            moving_pipe(i + 1, j + 1, 1)
    elif idx == 2:
        if i+1 < n and grid[i+1][j] == 0:
            moving_pipe(i+1,j,2)
        if j+1 < n and i+1 < n and grid[i+1][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j+1] == 0:
            moving_pipe(i+1,j+1,1)

moving_pipe(0,1,0)

print(cnt)
