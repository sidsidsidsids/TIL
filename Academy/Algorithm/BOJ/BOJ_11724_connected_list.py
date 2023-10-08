N, M = map(int,input().split())
if M == 0:
    print(N)
else:
    adjL = [ [] for _ in range(N+1) ]

    for _ in range(M):
        a, b = map(int,input().split())
        adjL[a].append(b)
        adjL[b].append(a)

    def connect_count(start):
        cnt = 0
        visited = [-1] + [0] * N
        stack = [start]
        visited[start] = 1

        while visited.count(0):
            while stack:
                elem = stack.pop()
                for goal in adjL[elem]:
                    if visited[goal] == 0:
                        visited[goal] = 1
                        stack.append(goal)
            if visited.count(0):
                idx = visited.index(0)
                visited[idx] = 1
                stack.append(idx)
                cnt += 1

        return cnt + 1

    print(connect_count(1))