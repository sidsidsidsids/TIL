N, M = map(int,input().split())
maze = [ list(map(int,input())) for _ in range(N) ]
visited = [ [0] * M for _ in range(N) ]

def BFS(a,b):
    Q = [[a,b]]
    visited[a][b] = 1

    while Q:
        location = Q.pop(0)
        y, x = location[0], location[1]
        for dy, dx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
            if 0 <= dy < N and 0 <= dx < M:
                if maze[dy][dx] == 1 and visited[dy][dx] == 0:
                    visited[dy][dx] = visited[y][x] + 1
                    Q.append([dy,dx])

                    if dy == N-1 and dx == M-1:
                        return visited[dy][dx]

print(BFS(0,0))