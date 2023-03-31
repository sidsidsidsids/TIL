'''
큰 거 먼저 찾기
'''

grid = [ list(map(int,input().split())) for _ in range(10) ]
board = [0, 0, 0, 0, 0]
ans = 0

def attach(i,j):
    global board
    global ans

    k = 2
    s = 1
    # 붙일 종이 크기 판정
    while True:
        for i_k in range(k):
            if s == 0 :
                break
            for j_k in range(k):
                if grid[i+i_k][j+j_k] == 0:
                    s = 0
                    break
        if s == 0:
            break
        k += 1
        if k > 5:
            break
    # 붙일 종이 정했으면 리스트 반영
    k = k-1
    board[k-1] += 1
    # 붙인 곳 0으로
    for ik in range(k):
        for jk in range(k):
            grid[i+ik][j+jk] = 0
    # board 판정
    for b in range(5):
        if board[b] > 5:
            ans = -1
            return ans
    ans += 1
    return ans



ss = 1
for y in range(10):
    if ss == 0:
        break
    for x in range(10):
        if grid[y][x]:
            attach(y,x)
            if ans == -1:
                ss = 0
                break

if ss:
    print(ans)
else:
    print(-1)

