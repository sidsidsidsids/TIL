'''
총 10개의 테스트 케이스
'A' 'B' 'C'로 주어진 글자판(8*8)에서 팰린드롬 찾기

입력 : 팰린드롬 글자 수, 글자판
출력 : 테스트 케이스, 팰린드롬 개수

위에서 아래로, 가로로 왼쪽에서 오른쪽으로 회문판별
왼쪽에서 오른쪽으로, 세로로 위에서 아래로 회문판별
'''
import sys
sys.stdin = open("input.txt", "r")

test_case = 1
for _ in range(10):
    length = int(input())
    board = []
    cnt = 0
    for _ in range(8): # 글자판 입력
        board.append(list(map(str,input())))
    # 가로
    for i in range(8):
        for j in range(8-length+1):
            if board[i][j:j+length] == list(reversed(board[i][j:j+length])):
                cnt += 1
    # 세로
    for j in range(8):
        for i in range(8-length+1):
            sero = []
            for k in range(length):
                sero.append(board[i+k][j])
            if sero == list(reversed(sero)):
                cnt += 1
    print(f'#{test_case}', cnt)
    test_case += 1
