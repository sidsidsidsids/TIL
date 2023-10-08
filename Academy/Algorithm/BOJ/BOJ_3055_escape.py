import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int,input().split())
grid = [ list(map(str,input())) for _ in range(R) ]

water = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'S':
            start = [i,j]
        elif grid[i][j] == '*':
            water.append([i,j])

def escape(dochi,water):
    d_Q = deque()
    d_Q.append(dochi)
    V = [ [0]*C for _ in range(R) ]
    V[dochi[0]][dochi[1]] = 1
    old_d = 1
    new_d = 0
    cnt = 0

    if water:
        w_Q = deque()
        for a,b in water:
            w_Q.append([a,b])
            V[a][b] = -1
        old_w = len(water)
        new_w = 0


        while d_Q:
            while old_w:
                elem = w_Q.popleft()
                y, x = elem[0], elem[1]
                old_w -= 1
                for ny, nx in [[y+1,x],[y-1,x],[y,x-1],[y,x+1]]:
                    if 0<=ny<R and 0<=nx<C and V[ny][nx] == 0:
                        if grid[ny][nx] != 'D' and grid[ny][nx] != 'X':
                            V[ny][nx] = -1
                            w_Q.append([ny,nx])
                            new_w += 1
            old_w += new_w
            new_w = 0

            while old_d:
                elem = d_Q.popleft()
                y, x = elem[0], elem[1]
                old_d -= 1
                for ny, nx in [[y + 1, x], [y - 1, x], [y, x - 1], [y, x + 1]]:
                    if 0 <= ny < R and 0 <= nx < C and V[ny][nx] == 0:
                        if grid[ny][nx] != 'X':
                            if grid[ny][nx] == 'D':
                                return cnt + 1
                            else:
                                V[ny][nx] = 1
                                d_Q.append([ny,nx])
                                new_d += 1
            old_d += new_d
            new_d = 0
            cnt += 1

        return 'KAKTUS'

    else:
        while d_Q:
            elem = d_Q.popleft()
            y, x = elem[0], elem[1]
            old_d -= 1
            for ny, nx in [[y + 1, x], [y - 1, x], [y, x - 1], [y, x + 1]]:
                if 0 <= ny < R and 0 <= nx < C and V[ny][nx] == 0:
                    if grid[ny][nx] != 'X':
                        if grid[ny][nx] == 'D':
                            return cnt + 1
                        else:
                            V[ny][nx] = 1
                            d_Q.append([ny, nx])
                            new_d += 1
            if old_d == 0:
                old_d += new_d
                new_d = 0
                cnt += 1
        return 'KAKTUS'


print(escape(start,water))




'''
visited = [ [0]*C for _ in range(R) ]

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'X':
            visited[i][j] = -2
        elif grid[i][j] == 'D':
            goal = [i,j]
        elif grid[i][j] == 'S':
            start = [i,j]
        elif grid[i][j] == '*':
            water = [i,j]

def BFS_with_two(a,b,c,d):
    wQ = deque()
    wQ.append([c,d])
    goQ = deque()
    goQ.append([a,b])
    visited[c][d] = -1
    visited[a][b] = 1
    oldwQ = 1
    newwQ = 0
    oldgoQ = 1
    newgoQ = 0
    run = 0

    while goQ:
        while oldwQ:
            wwater = wQ.popleft()
            y, x = wwater[0], wwater[1]
            oldwQ -= 1
            for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
                if 0<=ny<R and 0<=nx<C and visited[ny][nx] != -2 and grid[ny][nx] != 'D':
                    visited[ny][nx] = -1
                    wQ.append([ny,nx])
                    newwQ += 1
        oldwQ += newwQ
        newwQ = 0

        while oldgoQ:
            go = goQ.popleft()
            i, j = go[0], go[1]
            oldgoQ -= 1
            for ni, nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=ni<R and 0<=nj<C:
                    if grid[ni][nj] == 'D':
                        return run + 1
                    elif visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        goQ.append([ni,nj])
                        newgoQ += 1
        oldgoQ += newgoQ
        newgoQ = 0
        run += 1

    return 'KAKTUS'

print(BFS_with_two(start[0],start[1],water[0],water[1]))
'''