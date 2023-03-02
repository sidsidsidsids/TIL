T = int(input())
test_cnt = 1
for _ in range(T):
    draw_time = int(input()) # 테스트 케이스 개수
    board = [[0] * 10 for _ in range(10)] # 전체판
    answer = 0 # 답안 저장용 변수
    duplicate = set() # 겹쳐 색칠한 곳을 기록할 set 선언
    for _ in range(draw_time): # 그릴 횟수 만큼
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if board[i][j] != 0: # 색칠한 곳을 또 색칠하면
                    if (i, j) in duplicate: # 세트에 좌표가 이미 있으면
                        continue
                    else: # 첫번째면
                        duplicate.add((i,j)) # 세트에 좌표 추가
                board[i][j] = color # 색칠하기
    print(f'#{test_cnt} {len(duplicate)}') # 세트에 있는 좌표의 개수 = 겹쳐 색칠한곳
    test_cnt += 1