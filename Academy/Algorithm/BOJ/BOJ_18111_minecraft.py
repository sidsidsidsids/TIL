'''
블록 파는데 2초
블록 설치하는데 1초
출력 : 시간, 가장 높은 땅 높이 (답이 여러 개일 경우 최소 시간에서 땅 높이가 가장 높은 경우 출력)

'''
N, M, inventory = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

block_total = 0
for i in range(N):
    block_total += sum(grid[i])

target = block_total // (N*M)
irregular = block_total % (N*M)

cnt = 0
gj = (target+1) * (N*M) - block_total
if inventory >= gj:
    if irregular >= (N*M)/3:
        for i in range(N):
            for j in range(M):
                if grid[i][j] < target+1:
                    while grid[i][j] < target+1:
                        grid[i][j] += 1
                        inventory -= 1
                        cnt += 1
                elif grid[i][j] > target+1:
                    while grid[i][j] > target+1:
                        grid[i][j] -= 1
                        inventory += 1
                        cnt += 2
    else:
        for i in range(N):
            for j in range(M):
                if grid[i][j] > target:
                    while grid[i][j] > target:
                        grid[i][j] -= 1
                        inventory += 1
                        cnt += 2
                elif grid[i][j] < target:
                    while grid[i][j] < target:
                        grid[i][j] += 1
                        inventory -= 1
                        cnt += 1
else:
    for i in range(N):
        for j in range(M):
            if grid[i][j] > target:
                while grid[i][j] > target:
                    grid[i][j] -= 1
                    inventory += 1
                    cnt += 2

    for i in range(N):
        for j in range(M):
            if grid[i][j] < target and inventory:
                while grid[i][j] < target:
                    grid[i][j] += 1
                    inventory -= 1
                    cnt += 1

print(cnt, grid[0][0])
