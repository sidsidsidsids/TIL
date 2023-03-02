test_case = int(input())
for tc in range(1, test_case+1):
    board = [ list(map(str,input())) for _ in range(5) ]

    # max len
    max_len = 0
    for i in range(5):
        if max_len < len(board[i]):
            max_len = len(board[i])

    answer = ''
    while True:
        for i in range(5):
            if board[i]:
                letter = board[i].pop(0)
                answer += letter
        if len(board[0]) == len(board[1]) == len(board[2]) == len(board[3]) == len(board[4]) == 0:
            break

    print(f'#{tc} {answer}')
