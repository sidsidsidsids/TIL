def dfs(v):
    visited[v] = 1
    # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
    for w in range(1, V + 1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs(w)

test_cases = int(input())

for tc in range(test_cases):
    V, E = map(int, input().split())
    arr = []
    for i in range(E):
        s_node, e_node = map(int, input().split())
        arr.append(s_node)
        arr.append(e_node)

    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    # adjL = [[] for _ in range(V + 1)]

    visited = [0] * (V + 1)

    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjM[v1][v2] = 1
        # adjM[v2][v1] = 1  # v1과 v2는 인접해있다

        # adjL[v1].append(v2)
        # adjL[v2].append(v1)
    S, G = map(int,input().split())
    dfs(S)
    if visited[G] == 0:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')