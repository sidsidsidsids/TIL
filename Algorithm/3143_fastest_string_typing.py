test_cases = int(input())
for tc in range(test_cases):
    A, B = map(str,input().split())
    cnt = 0
    while B in A:
        A = A.replace(B,'',1)
        cnt += 1
    cnt += len(A)
    print(f'#{tc+1} {cnt}')