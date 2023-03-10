from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s_arr = [0] * (N+M)
f_arr = [0] * (N+M)


for i in range(N):
    u, v = map(int,input().split())
    s_arr[i] = u
    f_arr[i] = v
for i in range(M):
    u, v = map(int, input().split())
    s_arr[i+N] = u
    f_arr[i+N] = v

def BFS_100(position):
    cnt = 0
    s = 0
    Q = deque()
    Q.append(position)
    visited = [0] * 101

    oldQ = 1
    newQ = 0

    while Q and s == 0:
        start = Q.popleft()
        visited[start] = 1
        oldQ -= 1
        while start in s_arr:
            idx = s_arr.index(start)
            start = f_arr[idx]
        for i in range(1,7):
            if visited[start+i] == 0:
                Q.append(start+i)
                newQ += 1
                if start+i >= 100:
                    s = 1
                    break
        if s == 1:
            break

        if oldQ == 0:
            oldQ = newQ
            newQ = 0
            cnt += 1

    return cnt
print(BFS_100(1)+1)
