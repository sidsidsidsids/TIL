R, C = map(int,input().split())
grid = [ list(map(str,input())) for _ in range(R) ]

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
    wQ = [[c,d]]
    goQ = [[a,b]]
    visited[c][d] = -1
    visited[a][b] = 1
    oldwQ = 1
    newwQ = 0
    oldgoQ = 1
    newgoQ = 0
    run = 0

    while goQ:
        while oldwQ:
            wwater = wQ.pop(0)
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
            go = goQ.pop(0)
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