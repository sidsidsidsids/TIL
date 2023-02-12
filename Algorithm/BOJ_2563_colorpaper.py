board = [ [0] * 100 for _ in range(100) ]
papers = int(input())
for _ in range(papers):
    horizontal, vertical = map(int,input().split())
    for k in range(10):
        for l in range(10):
            board[vertical - k][horizontal + l] = 1

cnt = 0
for i in range(100):
    cnt += board[i].count(1)
print(cnt)