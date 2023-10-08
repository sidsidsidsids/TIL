def DFS(s):

    visited_d[s] = 1

    print(s, end=' ')

    for v in range(1, V+1):
        if arrM[s][v] == 1 and visited_d[v] == 0:
            DFS(v)
def BFS(s):
    visited = [0]*(V+1)
    q = [s]
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t, end=' ')
        for v in arrL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1
    return
V, E, S = map(int,input().split())
arrM = [ [0] * (V+1) for _ in range(V+1) ]
visited_d = [0]*(V+1)
arrL = [ [] for _ in range(V+1) ]
for _ in range(E):
    v1, v2 = map(int,input().split())
    arrM[v1][v2] = 1
    arrM[v2][v1] = 1
    arrL[v1].append(v2)
    arrL[v2].append(v1)
for i in range(V+1):
    arrL[i].sort()
DFS(S)
print()
BFS(S)
