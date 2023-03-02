import sys

N, M = map(int,sys.stdin.readline().split())
if M == 0:
    print(N)
else:
    adjL = [ [] for _ in range(N+1) ]

    for _ in range(M):
        a, b = map(int,sys.stdin.readline().split())
        adjL[a].append(b)
        adjL[b].append(a)

    def connect_count(start):
        cnt = 0
        visited = [-1] + [False] * N
        stack = [start]
        visited[start] = 1

        while visited.count(False):
            while stack:
                elem = stack.pop()
                for goal in adjL[elem]:
                    if visited[goal] == False:
                        stack.append(goal)
                        visited[goal] = True
            if visited.count(False):
                idx = visited.index(False)
                stack.append(idx)
                cnt += 1

        return cnt + 1

    print(connect_count(1))