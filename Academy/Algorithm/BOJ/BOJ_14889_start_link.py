'''
grid[i][j] + grid[j][i]
조합 뽑아서 브루트포스?

'''
from itertools import combinations

N = int(input())
grid = [ list(map(int,input().split())) for _ in range(N) ]

players = [i+1 for i in range(N)]
subset = list(combinations(players,N//2))

ans = 100

for i in range(len(subset)//2):
    start_score = 0
    start = []
    for player in subset[i]:
        start.append(player)
    s_subset = list(combinations(start,2))
    for a, b in s_subset:
        start_score += grid[a-1][b-1]
        start_score += grid[b-1][a-1]

    link_score = 0
    link = []
    for player in subset[-(i+1)]:
        link.append(player)
    l_subset = list(combinations(link,2))
    for a, b in l_subset:
        link_score += grid[a-1][b-1]
        link_score += grid[b-1][a-1]

    if ans > abs(start_score - link_score):
        ans = abs(start_score - link_score)

print(ans)