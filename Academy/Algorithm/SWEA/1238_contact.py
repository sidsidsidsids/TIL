def BFS(s):
    visited = [0] * (max(arr)+1)
    q = [s]
    visited[s] = 1

    while q:
        t = q.pop(0)
        for v in adjL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t] + 1

    maximum = max(visited)
    max_num = 0
    for i in range(len(visited)):
        if visited[i] == maximum:
            max_num = i

    return max_num


for tc in range(1,11):
    E2, S = map(int,input().split())
    arr = list(map(int,input().split()))

    adjL = [ [] for _ in range(max(arr) + 1) ]

    for i in range(E2//2):
        v1, v2 = arr[2*i], arr[2*i + 1]
        if v2 in adjL[v1]:
            continue
        else:
            adjL[v1].append(v2)

    print(f'#{tc} {BFS(S)}')

