# M, N = map(int,input().split())
# spaces = [0] * M
# for m in range(M):
#     space = list(map(int,input().split()))
#     spaceScale = sorted(enumerate(space), key=lambda X:X[1])
#     shape = [0] * N
#     for n in range(N):
#         shape[n] = spaceScale[n][0]
#     spaces[m] = shape
#
# cnt = 0
# for i in range(M-1):
#     for j in range(i+1,M):
#         if spaces[i] == spaces[j]:
#             cnt += 1
#
# print(cnt)

import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    # print(keys)
    ranks = {keys[i]: i for i in range(len(keys))}
    # print(ranks)
    add = tuple([ranks[x] for x in planets])
    # print(add)
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)