test_cases = int(input())
for tc in range(test_cases):
    board = [list(map(int,input().split())) for _ in range(9)]
    answer = 1
    # 블럭 체크
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[i+k][j+l])
            if len(set(block)) != 9:
                answer = 0
    # 가로 체크
    for i in range(9):
        garo = []
        for j in range(9):
            garo.append(board[i][j])
        if len(set(garo)) != 9:
            answer = 0
    # 세로 체크
    for j in range(9):
        sero = []
        for i in range(9):
            sero.append(board[i][j])
        if len(set(sero)) != 9:
            answer = 0

    print(f'#{tc+1} {answer}')