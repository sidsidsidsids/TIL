N, M = input().split()
N = int(N)
M = int(M)
world = [[] for _ in range(N)]
for n in range(N):
    world[n] = list(input())

for i in range(N):
    for j in range(M):
        if 