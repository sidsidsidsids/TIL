'''
1 : +
2 : |
3 : ㅡ
4 : ㄴ
5 : 「
6 : ㄱ
7 : 」
맨홀뚜껑 : 시작점
있을 수 있는 장소의 수 구하기
- 한 시간일 때 맨홀 위치만, 두 시간이면 맨홀 인접 구역 중 가능한 구역까지
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    # 지도의 세로 가로 길이, 맨홀의 세로 가로 좌표, 탈출 후 소요 시간
    N, M, R, C, L = map(int,input().split())
    # 지도
    grid = [ list(map(int,input().split())) for _ in range(N) ]
    # 방문기록
    visited = [ [0] * M for _ in range(N) ]
    # 시작점 grid[R][C]
    y_list = [R]
    x_list = [C]
    cnt = 1
    while L > 1:
        y_tmp = []; x_tmp = []
        while x_list:
            R = y_list.pop(0)
            C = x_list.pop(0)
            visited[R][C] = 1

            if grid[R][C] == 1:
                # 상
                if 0 <= R-1 < N and grid[R-1][C] in [1,2,5,6]:
                    if visited[R-1][C] == 0:
                        cnt += 1
                        y_tmp.append(R-1)
                        x_tmp.append(C)
                # 하
                if 0 <= R+1 < N and grid[R+1][C] in [1,2,4,7]:
                    if visited[R+1][C] == 0:
                        cnt += 1
                        y_tmp.append(R+1)
                        x_tmp.append(C)
                # 좌
                if 0 <= C-1 < M and grid[R][C-1] in [1,3,4,5]:
                    if visited[R][C-1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C-1)
                # 우
                if 0 <= C+1 < M and grid[R][C+1] in [1,3,6,7]:
                    if visited[R][C+1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C+1)

            elif grid[R][C] == 2:
                # 상
                if 0 <= R-1 < N and grid[R-1][C] in [1,2,5,6]:
                    if visited[R-1][C] == 0:
                        cnt += 1
                        y_tmp.append(R-1)
                        x_tmp.append(C)
                # 하
                if 0 <= R+1 < N and grid[R+1][C] in [1,2,4,7]:
                    if visited[R+1][C] == 0:
                        cnt += 1
                        y_tmp.append(R+1)
                        x_tmp.append(C)

            elif grid[R][C] == 3:
                # 좌
                if 0 <= C - 1 < M and grid[R][C - 1] in [1,3, 4, 5]:
                    if visited[R][C-1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C - 1)
                # 우
                if 0 <= C + 1 < M and grid[R][C + 1] in [1,3, 6, 7]:
                    if visited[R][C+1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C + 1)

            elif grid[R][C] == 4:
                # 상
                if 0 <= R - 1 < N and grid[R-1][C] in [1, 2, 5, 6]:
                    if visited[R-1][C] == 0:
                        cnt += 1
                        y_tmp.append(R - 1)
                        x_tmp.append(C)
                # 우
                if 0 <= C + 1 < M and grid[R][C + 1] in [1, 3, 6, 7]:
                    if visited[R][C+1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C + 1)

            elif grid[R][C] == 5:
                # 하
                if 0 <= R + 1 < N and grid[R+1][C] in [1, 2, 4, 7]:
                    if visited[R+1][C] == 0:
                        cnt += 1
                        y_tmp.append(R + 1)
                        x_tmp.append(C)
                # 우
                if 0 <= C + 1 < M and grid[R][C + 1] in [1, 3, 6, 7]:
                    if visited[R][C+1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C + 1)

            elif grid[R][C] == 6:
                # 하
                if 0 <= R + 1 < N and grid[R+1][C] in [1, 2, 4, 7]:
                    if visited[R+1][C] == 0:
                        cnt += 1
                        y_tmp.append(R + 1)
                        x_tmp.append(C)
                # 좌
                if 0 <= C - 1 < M and grid[R][C - 1] in [1, 3, 4, 5]:
                    if visited[R][C-1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C - 1)

            elif grid[R][C] == 7:
                # 상
                if 0 <= R - 1 < N and grid[R-1][C] in [1, 2, 5, 6]:
                    if visited[R-1][C] == 0:
                        cnt += 1
                        y_tmp.append(R - 1)
                        x_tmp.append(C)
                # 좌
                if 0 <= C - 1 < M and grid[R][C - 1] in [1, 3, 4, 5]:
                    if visited[R][C-1] == 0:
                        cnt += 1
                        y_tmp.append(R)
                        x_tmp.append(C - 1)
        y_list = y_tmp
        x_list = x_tmp
        L -= 1
    print(f'#{tc} {cnt}')
