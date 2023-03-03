N, M = map(int,input().split())
adjL = [ [] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int,input().split())
    if b in adjL[a]:
        pass
    else:
        adjL[a].append(b)
    if a in adjL[b]:
        pass
    else:
        adjL[b].append(a)

def BFS(s):
    visited = [0] + [-1] * N

    visited[s] = 0
    Q = [s]

    while Q:
        elem = Q.pop(0)
        for r in adjL[elem]:
            if visited[r] == -1:
                visited[r] = visited[elem] + 1
                Q.append(r)

    return sum(visited)

low_val = 0
for i in range(1,N+1):
    value = BFS(i)
    if low_val == 0:
        low_val = value
        ans = i
    elif value < low_val:
        low_val = value
        ans = i

print(ans)
