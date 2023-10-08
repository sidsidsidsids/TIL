'''
왼쪽 위 꼭짓점에서 <- 어떻게?
    1. 해당 인덱스가 값을 가지고 왼쪽과 위가 인덱스 밖
    2. 해당 인덱스가 값을 가지고 왼쪽이 0 , 위가 인덱스 밖
    3. 해당 인덱스가 값을 가지고 왼쪽이 인덱스 밖, 위가 0
    4. 해당 인덱스가 값을 가지고 왼쪽과 위가 0

꼭짓점을 찾으면
    0이 나올때까지 i 증가시키다가 0 나오면 그 전 i값 저장
    0이 나올때까지 j 증가시키다가 0 나오면 그 전 j값 저장
'''
test_case = int(input())
for tc in range(test_case):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    i = 0; j = 0
    box_i = []; box_j = []
    while i <= n-1 and j < n: # board의 끝까지 갈 때 까지
        if (board[i][j] != 0 and j - 1 < 0 and i-1 < 0) or (board[i][j] != 0 and board[i][j-1] == 0 and i-1 < 0) or (board[i][j] != 0 and j-1 < 0 and board[i-1][j] == 0) or (board[i][j] != 0 and board[i][j-1] == 0 and board[i-1][j] == 0):
            #위 4가지 경우중 하나라도 발생하면)
            for k in range(n): # 가로 크기 재기
                if j+k > n-1:
                    box_j.append(k)
                    break
                if board[i][j+k] == 0:
                    box_j.append(k)
                    break
            for k in range(n): # 세로 크기 재기
                if i+k > n-1:
                    box_i.append(k)
                    break
                if board[i+k][j] == 0:
                    box_i.append(k)
                    break
        # 이동
        if j == n-1: # 오른쪽 끝까지 간다면
            j = -1
            i += 1 # 한 줄 밑 왼쪽 끝으로 좌표 변경
        j += 1  # 오른쪽으로 탐색

    box_pair = {}
    for l in range(len(box_i)):
        box_pair[box_i[l], box_j[l]] = box_i[l]*box_j[l]
    sort_box_pair = sorted(box_pair.keys(), key = lambda X :(box_pair[X], X[0]))
    answer = []
    for i in range(len(sort_box_pair)):
        answer.append(sort_box_pair[i][0])
        answer.append(sort_box_pair[i][1])
    print(f'#{tc+1} {len(sort_box_pair)}', *answer)
