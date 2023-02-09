board = [[0] * 100 for _ in range(100)]
for _ in range(4):
    left_i, left_j, right_i, right_j = map(int,input().split())
    i_k = right_i - left_i
    j_k = right_j - left_j
    for i in range(i_k):
        for j in range(j_k):
            board[left_i + i][left_j + j] = 1
cnt = 0
for i in range(100):
    cnt += board[i].count(1)
print(cnt)