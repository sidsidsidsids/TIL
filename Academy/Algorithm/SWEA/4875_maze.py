# def dfs(i, j):
#
#     visited[i][j] = 1
#
#     for y, x in [[i-1 , j],[i, j-1],[i+1, j],[i, j+1]]:
#         if 0 <= y < N and 0 <= x < N:
#             if maze[y][x] == 3:
#                 global s
#                 s = 1
#             elif maze[y][x] == 0 and visited[y][x] == 0:
#                 dfs(y, x)
#     return s
#
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     maze = [ list(map(int,input())) for _ in range(N) ]
#     s = 0
#
#     visited = [ [0]*N for _ in range(N) ]
#
#     # 시작 좌표
#     for t in range(len(maze)):
#         if 2 in maze[t]:
#             start_i = t
#             start_j = maze[t].index(2)
#     #print(start_i, start_j)
#
#     print(f'#{tc+1} {dfs(start_i, start_j)}')

def DFS(a,b):
    stack = [[a,b]]
    visit[a][b] = 1

test_case = int(input())
for tc in range(1,test_case+1):
    n = int(input())
    maze = [ list(map(int,input())) for _ in range(n) ]

    visit = [ [0] * n for _ in range(n) ]




