import itertools

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

comb = itertools.combinations(M_grid,M)
print(comb)

def BFS(*a):
    Q = [*a]
    v = visited[:]
    print(Q)
    v[a[0]][a[1]] = 1

    while Q:
        loc = Q.pop(0)
        y, x = loc[0], loc[1]
        max_val = 0

        for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
            if 0 <= ny < N and 0 <= nx < N:
                if v[ny][nx] == 0:
                    v[ny][nx] += v[y][x] + 1
                    max_val = v[ny][nx]
                    Q.append([ny,nx])

    if 0 in v:
        return -1
    else:
        return max_val - 1

min = 100
for i in comb:
    if BFS(i) == -1:
        s = 1
        pass
    if BFS(i) < min:
        min = BFS(i)

if min == 100:
    print(-1)
else:
    print(min)


