'''
N극에서 멀어지는 빨강(1)은 아래로
S극에서 멀어지는 파랑(2)은 위로
겹치면 교착상태 (여러개 겹친 건 하나로 침)
안겹치면 떨어짐

입력 : 한 변의 길이(100 고정), 테이블 상태
출력 : 테스트 케이스 번호, 교착 개수

세로로 새로 리스트를 만들어서 한 줄씩 비교?
    이 때 빨강(1)의 인덱스는 증가, 파랑(2)의 인덱스는 감소
'''

import sys
sys.stdin = open("input.txt", "r")
test_case = 1
for _ in range(10):
    N = int(input())
    board = []
    answer = 0
    for _ in range(100): # 글자판 입력
        board.append(list(map(int,input().split())))
    for j in range(100):
        check_line = []
        for i in range(100):
            check_line.append(board[i][j]) # 세로로 입력받기
        i = 0
        while i <= 99:
            if check_line[i] == 1:
                for j in range(1,100-i):
                    if i+j > 99:
                        break
                    elif check_line[i+j] == 2:
                        answer += 1
                        break
                i += j
            i += 1
    print(f'#{test_case} {answer}')
    test_case += 1

