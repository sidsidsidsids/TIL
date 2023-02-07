'''
입력값 : 테스트 케이스 수, N(맵 크기) M(파리채 범위), N*N 숫자 배열
출력값 : #테스트 케이스 번호, 잡은 파리 합
'''
test_case = int(input())
for tc in range(test_case):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    max_catch = 0
    for i in range(N-M):
        for j in range(N-M):
            catch = 0
            for k in range(M):
                for l in range(M):
                    catch += board[i+k][j+l]
            if catch > max_catch:
                max_catch = catch
    print(f'#{tc+1} {max_catch}')