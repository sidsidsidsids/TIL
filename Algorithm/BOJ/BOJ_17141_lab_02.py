N, M = map(int,input().split())
lab = [ list(map(int,input().split())) for _ in range(N) ]

M_grid = [ [] for _ in range(N) ]
visited = [ [0]*N for _ in range(N) ]
grid_idx = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            M_grid[grid_idx] = [i, j]
            grid_idx += 1
        elif lab[i][j] == 1:
            visited[i][j] = -1

def BFS(a,b):
    Q = [[a,b]]
    visited[a][b] = 1

    while Q:
        loc = Q.pop(0)
        y, x = loc[0], loc[1]

        for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0:
                    visited[ny][nx] += visited[y][x] + 1
                    Q.append([ny,nx])

