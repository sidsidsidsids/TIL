N, K = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]
S, Y, X = map(int,input().split())
Y -= 1 ; X -= 1
visited = [[0] * N for _ in range(N)]
virus = []

if S == 0:
    if grid[Y][X] != 0:
        virus = [grid[Y][X]]
else:
    while S:
        if grid[Y][X] != 0:
            virus = [grid[Y][X]]
            break
        check = [[Y,X]]
        visited[Y][X] = 1
        old = 1
        new = 0

        while check:
            if S == 0:
                break

            elem = check.pop(0)
            y, x = elem[0], elem[1]
            old -= 1

            for ny, nx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
                if 0 <= ny < N and 0 <= nx < N:
                    if visited[ny][nx] == 0:
                        if grid[ny][nx] != 0:
                            virus.append(grid[ny][nx])
                        visited[ny][nx] = 1
                        check.append([ny,nx])
                        new += 1

            if old == 0:
                if virus:
                    S = 0
                    break
                S -= 1
                old = new
                new = 0

if virus:
    print(min(virus))
else:
    print(0)