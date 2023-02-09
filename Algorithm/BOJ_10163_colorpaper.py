board = [[0] * 1001 for _ in range(1001)]
papers = int(input())
paper_board = []

for i in range(papers):
    start_i, start_j, i_len, j_len = map(int,input().split())
    for len_i in range(i_len):
        for len_j in range(j_len):
            board[start_i+len_i][start_j+len_j] = i+1

answer = [0]*papers
for i in range(1,papers+1):
    for j in range(1001):
        answer[i-1] += board[j].count(i)
for ans in answer:
    print(ans)