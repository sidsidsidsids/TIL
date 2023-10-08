'''
달팽이

입력값 : n (사각형 한 변 길이)

[0]을 n*n으로 해놓고

a 첫 행 부터 n개 입력
b 끝 열에서 n-1개 입력
c 마지막 행에서 거꾸로 n-1개 입력
d 첫 열에서 거꾸로 n-2개 입력

a' 두번째 행에서 n-2개 입력
b' 끝에서 두번째 열에서 n-3개 입력
c' 끝에서 두번째 행에서 거꾸로 n-3개 입력
d' 끝에서 두번째 열에서 거꾸로 n-4개 입력 ...

n = 홀수일 때 : 오른쪽으로 번호 넣으며 종료 (a'에서 n-k == 2일 때)
n = 짝수일 때 : 왼쪽으로 번호 넣으며 종료 (c'에서 n-k == 2일 때)
'''
test_case = int(input())
test_num = 1
for _ in range(test_case):
    n = int(input())
    squares = [[0]*n for _ in range(n)]
    i = 0; j = 0; number = 1

    for k in range(n-1,-1,-1):
        while j <= k:
            squares[i][j] = number
            number += 1
            j += 1
        j -= 1; i += 1
        while i <= k:
            squares[i][j] = number
            number += 1
            i += 1
        i -= 1; j -= 1
        while n-(k+1) <= j:
            squares[i][j] = number
            number += 1
            j -= 1
        j += 1; i -= 1
        while n-k <= i:
            squares[i][j] = number
            number += 1
            i -= 1
        i +=1; j += 1

    print(f'#{test_num}')
    for i in range(n):
        print(*squares[i])
    test_num += 1
