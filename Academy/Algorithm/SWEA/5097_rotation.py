test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))

    print(f'#{tc} {numbers[M%N]}')