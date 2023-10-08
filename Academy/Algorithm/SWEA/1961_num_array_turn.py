test_cases = int(input())
for tc in range(test_cases):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    ans1 = []
    for j in range(n):
        lists = []
        for i in range(n-1,-1,-1):
            lists.append(board[i][j])
        ans1.append(lists)

    ans2 = []
    for i in range(n-1,-1,-1):
        lists = []
        for j in range(n-1,-1,-1):
            lists.append(board[i][j])
        ans2.append(lists)

    ans3 = []
    for j in range(n-1,-1,-1):
        lists = []
        for i in range(n):
            lists.append(board[i][j])
        ans3.append(lists)

    print(f'#{tc+1}')
    for k in range(n):
        ans1[k] = ''.join(map(str,ans1[k]))
        ans2[k] = ''.join(map(str,ans2[k]))
        ans3[k] = ''.join(map(str,ans3[k]))
        print(ans1[k], ans2[k], ans3[k])

