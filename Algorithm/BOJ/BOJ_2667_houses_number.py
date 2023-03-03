N = int(input())
grid = [ list(map(int,input())) for _ in range(N) ]
visited = [ [0] * N for _ in range(N) ]
danji = 0

def DFS(i,j):
    stack = [[i,j]]
    visited[i][j] = 1
    house_cnt = 1

    while stack:
        location = stack.pop()
        a, b = location[0], location[1]
        for di, dj in [[a+1,b],[a-1,b],[a,b+1],[a,b-1]]:
            if 0 <= di < N and 0 <= dj < N:
                if visited[di][dj] == 0 and grid[di][dj] == 1:
                    stack.append([di,dj])
                    visited[di][dj] = 1
                    house_cnt += 1
    global danji
    danji += 1

    return house_cnt

houses_amount = []
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0 and grid[y][x] == 1:
            numbering = DFS(y,x)
            houses_amount.append(numbering)
houses_amount.sort()
print(danji)
for n in houses_amount:
    print(n)

