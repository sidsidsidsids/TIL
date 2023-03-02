'''
글자판(N*N)에서 팰린드롬 찾아 출력하기

입력 : 테스트 케이스 / N(판 크기), M(회문 글자수) / 글자들
출력 : 테스트 케이스 번호, 회문 글자

위에서 아래로, 가로로 왼쪽에서 오른쪽으로 회문판별
왼쪽에서 오른쪽으로, 세로로 위에서 아래로 회문판별
'''
import sys
sys.stdin = open("sample_input.txt", "r")

test_cases = int(input())
for tc in range(test_cases):
    N, M = map(int,input().split())
    board = []
    answer = []
    for _ in range(N):
        s = input()
        s = ''.join(s)
        board.append(list(s))
    # 가로 부터
    for i in range(N):
        for j in range(N-M+1):
            if board[i][j:j + M] == list(reversed(board[i][j:j + M])):
                answer = board[i][j:j + M]
                break
    # 세로
    for j in range(N):
        if len(answer) != 0:
            break
        for i in range(N - M + 1):
            sero = []
            for k in range(M):
                sero.append(board[i + k][j])
            if sero == list(reversed(sero)):
                answer = sero
                break

    answer_letter = ''
    for word in answer:
        answer_letter += word

    print(f'#{tc+1} {answer_letter}')