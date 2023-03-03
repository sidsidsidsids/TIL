N = int(input())
route = [[-1] * (N+1)] + [ [-1] + list(map(int,input().split())) for _ in range(N) ]

def DFS(s):
    stack = [s]
    visit = [-1] + [0] * N

    while stack:
        go = stack.pop()
        for r in range(N+1):
            if visit[r] == 0 and route[go][r] == 1:
                stack.append(r)
                visit[r] = 1

    return visit[1:]

for i in range(1,N+1):
    print(*DFS(i))