'''
가능한 조합 중 합이 가장 작은 거 찾기
'''

def sum_with_nRook(i, j, N):
    able_case = []
    j_list = []
    for i in range(n):
        while 




test_case = int(input())
for tc in range(1,test_case+1):
    N = int(input())
    board = [ list(map(int,input().split())) for _ in range(N) ]

    bit = [ [0]*N for _ in range(N) ]

    sum_with_nRook(0,0,N)

    total_sum = []
    # # 최소값 좌표 찾기
    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j] < minimum:
    #             minimum = board[i][j]
    #             y = i
    #             x = j
    # total_sum += minimum
    # for i in range(len(board)):
    #     del board[i][x]
    # del board[y]


    print(f'#{tc} {total_sum}')