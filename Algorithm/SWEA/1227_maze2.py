'''
def dfs(i, j):

    visited[i][j] = 1

    for y, x in [[i-1 , j],[i, j-1],[i+1, j],[i, j+1]]:
        if 0 <= y < N and 0 <= x < N:
            if maze[y][x] == 3:
                global s
                s = 1
            elif maze[y][x] == 0 and visited[y][x] == 0:
                dfs(y, x)
    return s

#test_case = int(input())
for tc in range(1,11):
    test_c = int(input())
    N = 100
    maze = [ list(map(int,input())) for _ in range(N) ]
    s = 0

    visited = [ [0]*N for _ in range(N) ]

    # 시작 좌표
    for t in range(len(maze)):
        if 2 in maze[t]:
            start_i = t
            start_j = maze[t].index(2)
    #print(start_i, start_j)

    print(f'#{test_c} {dfs(start_i, start_j)}')
'''
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
    N = 100
    tc = int(input())
    maze = [ list(map(int,input())) for _ in range(N) ]

    maze_unpack = sum(maze, [])
    maze_start_idx = maze_unpack.index(2)
    start_i = maze_start_idx // 100
    start_j = maze_start_idx % 100
    print(start_i, start_j)
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j] == 2:
    #             start_i, start_j = i, j

    print(f'#{tc} {maze_bfs(start_i, start_j, N)}')