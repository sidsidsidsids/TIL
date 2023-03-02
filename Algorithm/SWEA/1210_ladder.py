'''
100 * 100 2차원 배열로 주어진 사다리
-> 한 줄에 100개씩 입력을 받음
좌표 : data[i][j]
i == 99일 때 목적지
2(목적지)에 가기 위한 출발지의 j 값을 출력
시작점 : data[99][j] 에서 사다리 거꾸로 타기

i 값이 0이 될 때 까지
    옆 칸에 1이 안나오면
        while 옆 칸에 1이 나올때까지
            i -= 1
    옆 칸에 1이 나오면
        while 이동 방향쪽 칸에 0이 나올때까지
            j += 1 or j -= 1
        i -= 1 (0이 나오면 왔던길 다시 되돌아가지 않게 위로)

i == 0 일 때의 j 값 구하기
'''
for _ in range(10):

    test_num = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int,input().split())))
    i = 99 # 맨 마지막 리스트 (맨 밑줄)
    j = ladder[99].index(2) # 값이 2인 인덱스 구하기 (시작점)

    while i > 0:
        if j == 0:
            if ladder[i][j+1] == 0:
                i -= 1
            else:
                while ladder[i][j+1] != 0:
                    j += 1
                i -= 1
        elif j == 99:
            if ladder[i][j-1] == 0:
                i -= 1
            else:
                while ladder[i][j-1] != 0:
                    j -= 1
                i -= 1
        else:
            if ladder[i][j-1] == 0 and ladder[i][j+1] == 0:
                i -= 1 # 양 옆이 1이 아니면 위로 올라가기
            else:
                if ladder[i][j-1] == 1:
                    while ladder[i][j-1] != 0:
                        j -= 1
                        if j == 0:
                            break
                    i -= 1
                else:
                    while ladder[i][j+1] != 0:
                        j += 1
                        if j == 99:
                            break
                    i -= 1

    print(f'#{test_num} {j}')