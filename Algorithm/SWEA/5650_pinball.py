'''
1 : ㄴ
2 : 『
3 : ㄱ
4 : 』
5 : ㅁ
6~10 : 웜홀 (같은 숫자로 이동, 기존 방향 유지)
-1, 시작 지점 : 종료
'''

def move(i,j,idx):
    if idx == 0:
        return i-1, j
    elif idx == 1:
        return i, j+1
    elif idx == 2:
        return i+1, j
    elif idx == 3:
        return i, j-1

def block_1(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 1
    elif ball_idx == 3:
        return 0

def block_2(ball_idx):
    if ball_idx == 0:
        return 1
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 2

def block_3(ball_idx):
    if ball_idx == 0:
        return 3
    elif ball_idx == 1:
        return 2
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 1

def block_4(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 0
    elif ball_idx == 2:
        return 3
    elif ball_idx == 3:
        return 1

def block_5(ball_idx):
    if ball_idx == 0:
        return 2
    elif ball_idx == 1:
        return 3
    elif ball_idx == 2:
        return 0
    elif ball_idx == 3:
        return 1

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    grid = [ list(map(int,input().split())) for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            for idx in range(4):

