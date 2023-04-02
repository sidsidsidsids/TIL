import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int,input().split())
world = [ list(map(int,input().split())) for _ in range(N) ]

def target(i,j,grid):
    global duplicate

    search = False

    for ni, nj in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
        if 0 <= ni < N and 0 <= nj < N and L <= abs(grid[i][j] - grid[ni][nj]) <= R:
            search = True

    if search:
        Q = deque()
        Q.append([i,j])
        result = []
        V = [ [0]*N for _ in range(N) ]
        V[i][j] = 1

        while Q:
            elem = Q.popleft()
            y, x = elem[0], elem[1]
            for ni, nj in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
                if 0 <= ni < N and 0 <= nj < N and V[ni][nj] == 0:
                    if L <= abs(grid[y][x] - grid[ni][nj]) <= R:
                        Q.append([ni,nj])
                        duplicate.append([ni,nj])
                        V[ni][nj] = 1
                        if not result:
                            result.append([i,j])
                        result.append([ni,nj])
        if result:
            result.sort(key = lambda X:(X[0],X[1]))
        return result
    else:
        return False

def union_move(countriess):
    for countries in countriess:
        people_sum = 0
        country_amount = 0
        for y, x in countries:
            people_sum += world[y][x]
            country_amount += 1
        amounts = people_sum//country_amount
        for y,x in countries:
            world[y][x] = amounts
    return

cnt = 0
while True:
    open = list()
    duplicate = list()

    for i in range(N):
        for j in range(N):
            if [i,j] not in duplicate:
                opens = target(i,j,world)
                if opens and opens not in open:
                    open.append(opens)
    if open:
        union_move(open)
        cnt += 1
    else:
        break

print(cnt)