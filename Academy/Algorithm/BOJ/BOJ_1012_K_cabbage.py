import sys
sys.setrecursionlimit(4000)

def DFS(y,x):
    visited[y][x] = 1
    for dy, dx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
        if 0 <= dy < sero and 0 <= dx < garo:
            if land[dy][dx] == 1 and visited[dy][dx] == 0:
                DFS(dy,dx)

test_case = int(input())
for _ in range(test_case):
    garo, sero, cabbages = map(int,input().split())
    land = [ [0] * garo for _ in range(sero) ]
    visited = [[0] * garo for _ in range(sero)]
    cnt = 0

    for _ in range(cabbages):
        x, y = map(int,input().split())
        land[y][x] = 1

    for i in range(sero):
        for j in range(garo):
            if land[i][j] == 1 and visited[i][j] == 0:
                DFS(i,j)
                cnt += 1

    print(cnt)