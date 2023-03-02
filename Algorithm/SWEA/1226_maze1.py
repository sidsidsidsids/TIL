def maze_bfs(i, j, N):
    visited = [ [0] * N for _ in range(N) ]
    q = [[i, j]]
    visited[i][j] = 1

    while q:
        t = q.pop(0)
        y, x = t[0], t[1]
        for a, b in [ [y-1, x], [y, x-1], [y+1, x], [y, x+1] ]:
            if 0 <= a < N and 0 <= b < N:
                if maze[a][b] == 0 and visited[a][b] == 0:
                    q.append([a,b])
                    visited[a][b] = visited[y][x] + 1
                elif maze[a][b] == 3:
                    return 1
    return 0

for _ in range(10):
    N = 16
    tc = int(input())
    maze = [ list(map(int,input())) for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j

    print(f'#{tc} {maze_bfs(start_i, start_j, N)}')
