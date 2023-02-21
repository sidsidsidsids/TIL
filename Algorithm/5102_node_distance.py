def node_distance_bfs(s,g):
    visited = [0] * (V+1)
    q = [s]
    visited[s] = 1

    while q:
        t = q.pop(0)
        for v in adjL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t] + 1
                if v == g:
                    return visited[v] - 1
    return 0


test_case = int(input())
for tc in range(1, test_case+1):
    V, E = map(int, input().split())

    adjL = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    S, G = map(int,input().split())

    print(f'#{tc} {node_distance_bfs(S,G)}')