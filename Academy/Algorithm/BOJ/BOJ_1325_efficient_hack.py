import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
grid = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    e, s = map(int,sys.stdin.readline().split())
    grid[s][e] = 1
ans = []
maxVal = 0
cnt = 0
for num in range(1, N+1):
    if sum(grid[num]):
        Q = deque()
        V = [0] * (N+1)
        Q.append(num)
        V[num] = 1
        cnt = 1
        while Q:
            elem = Q.pop()
            for nElem in range(N+1):
                if grid[elem][nElem] and not V[nElem]:
                    Q.append(nElem)
                    V[nElem] = 1
                    cnt += 1
        if cnt > maxVal:
            maxVal = cnt
            ans = [num]
        elif cnt == maxVal:
            ans.append(num)
print(*sorted(ans))

