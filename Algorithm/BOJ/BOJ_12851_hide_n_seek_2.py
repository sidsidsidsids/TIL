from collections import deque

N, K = map(int,input().split())

def finding(N,K):
    V = [0] * 200001
    Q = deque()
    Q.append(N)
    V[N] = 1

    old = 1
    new = 0
    cnt = 0
    goal = 0

    while Q:
        elem = Q.popleft()
        old -= 1

        for next in [elem - 1, elem + 1, elem * 2]:
            if 0 <= next <= 200000:
                if next == K:
                    goal += 1
                else:
                    if not V[next] or next == 2:
                        Q.append(next)
                        V[next] = 1
                        new += 1
        if old == 0:
            if goal:
                return [cnt+1, goal]
            old += new
            new = 0
            cnt += 1

if N == K:
    print(0)
    print(1)
else:
    result = finding(N,K)
    print(result[0])
    print(result[1])
