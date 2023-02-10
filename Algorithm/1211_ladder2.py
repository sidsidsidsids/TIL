'''
100 * 100 2차원 배열로 주어진 사다리
-> 한 줄에 100개씩 입력을 받음
좌표 : data[i][j]
i == 0 에서 시작하는 모든 길들 중에서
목적지까지 가장 짧은 길을 가지는 출발지 j 값을 출력
시작점 : data[0][j] 에서 사다리 타기

i 값이 99 될 때 까지 (움직일 때 마다 cnt += 1)
    옆 칸에 1이 안나오면
        while 옆 칸에 1이 나올때까지
            i += 1
    옆 칸에 1이 나오면
        while 이동 방향쪽 칸에 0이 나올때까지
            j += 1 or j -= 1
        i += 1 (0이 나오면 왔던길 다시 되돌아가지 않게 위로)

i == 99 일 때의 cnt 저장
가장 짧은 cnt를 가지는 출발값?
'''
import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):

    test_num = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int,input().split())))

    j_start=[] # 출발점 인덱스들
    for j in range(100):
        if ladder[0][j] == 1:
            j_start.append(j)

    cnt_min = 10000
    answer = 0
    i = 0  # 맨 첫 리스트 (맨 윗줄)

    for j in j_start: # 출발점들 순환
        cnt = 0
        start_pos = j # 초기 x좌표 저장
        while i < 99:
            if j == 0:
                if ladder[i][j+1] == 0:
                    i += 1
                    cnt += 1
                else:
                    while ladder[i][j+1] != 0:
                        j += 1
                        cnt += 1
                    i += 1
                    cnt += 1
            elif j == 99:
                if ladder[i][j-1] == 0:
                    i += 1
                    cnt += 1
                else:
                    while ladder[i][j-1] != 0:
                        j -= 1
                        cnt += 1
                    i += 1
                    cnt += 1
            else:
                if ladder[i][j-1] == 0 and ladder[i][j+1] == 0:
                    i += 1 # 양 옆이 1이 아니면 내려가기
                    cnt += 1
                else:
                    if ladder[i][j-1] == 1:
                        while ladder[i][j-1] != 0:
                            j -= 1
                            cnt += 1
                            if j == 0:
                                break
                        i += 1
                        cnt += 1
                    else:
                        while ladder[i][j+1] != 0:
                            j += 1
                            cnt += 1
                            if j == 99:
                                break
                        i += 1
                        cnt += 1
        if cnt < cnt_min:
            cnt_min = cnt
            answer = start_pos
        i = 0
    print(f'#{test_num} {answer}')