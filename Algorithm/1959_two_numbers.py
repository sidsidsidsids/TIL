test_case = int(input())
for tc in range(1,test_case + 1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    max_total = 0

    if N < M:
        for i in range(0,M - N + 1):
            total = 0
            for k in range(N):
                total += A[k] * B[i + k]
            if max_total < total:
                max_total = total
    elif N > M:
        for i in range(0,N - M + 1):
            total = 0
            for k in range(M):
                total += A[i + k] * B[k]
            if max_total < total:
                max_total = total
    else:
        for i in range(N):
            max_total = A[i] * B[i]

    print(f'#{tc} {max_total}')