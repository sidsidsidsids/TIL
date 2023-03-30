from collections import deque
import sys
input = sys.stdin.readline()

N, L, R = map(int,input().split())
world = [ list(map(int,input().split())) for _ in range(N) ]

def target(i,j,grid):
    Q = deque()
    Q.append([i,j])
    result = ([i,j])
    V = [ [0]*N for _ in range(N) ]
    V[i][j] = 1

    while Q:
        elem = Q.popleft()
        y, x = elem[0], elem[1]
        for ni, nj in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
            if 0 <= ni < N and 0 <= nj < N and V[ni][nj] == 0:
                if L <= abs(grid[y][x] - grid[ni][nj]) <= R:
                    Q.append([ni,nj])
                    V[ni][nj] = 1
                    result.append([ni,nj])

    return result

