import sys
sys.setrecursionlimit(10000)

n = int(input())
land = [ list(map(str,input())) for _ in range(n) ]
visited = [[0] * n for _ in range(n)]
cnt = 0

def R_DFS(y,x):
    visited[y][x] = 1
    for dy, dx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
        if 0 <= dy < n and 0 <= dx < n:
            if land[dy][dx] == 'R' and visited[dy][dx] == 0:
                R_DFS(dy,dx)
def G_DFS(y,x):
    visited[y][x] = 1
    for dy, dx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
        if 0 <= dy < n and 0 <= dx < n:
            if land[dy][dx] == 'G' and visited[dy][dx] == 0:
                G_DFS(dy,dx)
def B_DFS(y,x):
    visited[y][x] = 1
    for dy, dx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
        if 0 <= dy < n and 0 <= dx < n:
            if land[dy][dx] == 'B' and visited[dy][dx] == 0:
                B_DFS(dy,dx)
def RG_DFS(y,x):
    visited[y][x] = 1
    for dy, dx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
        if 0 <= dy < n and 0 <= dx < n:
            if (land[dy][dx] == 'R' or land[dy][dx] == 'G') and visited[dy][dx] == 0:
                RG_DFS(dy,dx)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if land[i][j] == 'R':
                R_DFS(i,j)
                cnt += 1
            elif land[i][j] == 'G':
                G_DFS(i,j)
                cnt += 1
            else:
                B_DFS(i,j)
                cnt += 1
normal = 0
normal += cnt

cnt = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if land[i][j] == 'B':
                B_DFS(i, j)
                cnt += 1
            else:
                RG_DFS(i, j)
                cnt += 1
RG = cnt
print(normal, RG)