T = 10
#여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    Max = 0
    for i in range(100):
        row = 0
        for j in range(100):
            row += arr[i][j]
        Max = max(Max, row)

    for j in range(100):
        col = 0
        for i in range(100):
            col += arr[i][j]
        Max = max(Max, col)

    diagonal1 = arr[0][0]
    delta_rightdown = [1, 1]
    next_row = 0
    next_col = 0

    for j in range(4):
        next_row = next_row + delta_rightdown[0]
        next_col = next_col + delta_rightdown[1]
        if 0 <= next_row < 100 and 0 <= next_col < 100:
            diagonal1 += arr[next_row][next_col]
    Max = max(Max, diagonal1)

    diagonal2 = arr[0][99]
    delta_leftdown = [1, -1]
    next_row2 = 0
    next_col2 = 99

    for j in range(100):
        for i in range(2):
            next_row2 = next_row2 + delta_leftdown[0]
            next_col2= next_col2 + delta_leftdown[1]
            if 0 <= next_row2 < 100 and 0 <= next_col2 < 100:
                diagonal2 += arr[next_row2][next_col2]
        Max = max(Max, diagonal2)

    print(f'#{test_case} {Max}')