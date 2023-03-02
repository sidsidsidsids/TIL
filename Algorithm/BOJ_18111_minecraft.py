'''
땅 파는데 2초
땅 메우는데 1초
출력 : 시간, 가장 높은 땅 높이 (답이 여러 개일 경우 최소 시간에서 땅 높이가 가장 높은 경우 출력)
'''
N, M, inventory = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

block_total = 0
for i in range(N):
    block_total += sum(grid[i])

