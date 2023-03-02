'''
중앙선을 잡고 그 기준으로
3*3 은 1줄 위 아래
5*5 은 2줄 위 아래
'''
test_cases = int(input())
for tc in range(test_cases):
    n = int(input())
    board = [list(map(int,input())) for _ in range(n)]
    k_value = n // 2
    profit = 0

    profit += sum(board[k_value])
    k = 1
    while k <= k_value:
        profit += sum(board[k_value - k][k:-k])
        k += 1
    k = 1
    while k <= k_value:
        profit += sum(board[k_value + k][k:-k])
        k += 1
    print(f'#{tc+1} {profit}')
