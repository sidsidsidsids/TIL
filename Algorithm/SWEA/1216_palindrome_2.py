'''
총 10개의 테스트 케이스
'A' 'B' 'C'로 주어진 글자판(100*100)에서 가장 긴 팰린드롬 찾기

입력 : 테스트 케이스 번호, 글자판
출력 : 테스트 케이스, 팰린드롬 글자 수

위에서 아래로, 가로로 왼쪽에서 오른쪽으로 회문판별
왼쪽에서 오른쪽으로, 세로로 위에서 아래로 회문판별
글자수를 큰거부터 하면 됨
'''
import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case = int(input())
    board = []
    answer = 0
    for _ in range(100): # 글자판 입력
        board.append(list(map(str,input())))
    for palindrome_length in range(99, -1, -1):
        # 가로
        for i in range(100):
            if answer != 0:
                break
            for j in range(100-palindrome_length+1):
                if board[i][j:j+palindrome_length] == list(reversed(board[i][j:j+palindrome_length])):
                    answer = palindrome_length
                    break
        # 세로
        for j in range(100):
            if answer != 0:
                break
            for i in range(100-palindrome_length+1):
                sero = []
                for k in range(palindrome_length):
                    sero.append(board[i+k][j])
                if sero == list(reversed(sero)):
                    answer = palindrome_length
                    break
    print(f'#{test_case}', answer)