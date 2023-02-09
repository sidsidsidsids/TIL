test_cases = int(input())
for tc in range(test_cases):
    A, B = map(str,input().split())
    cnt = 0

    while B in A: # 찾고자 하는 문자열이 A 안에 없을 때 까지
        A = A.replace(B,'',1) # 문자열을 찾을 때 마다 하나씩 지움
        cnt += 1 # 횟수 1회 증가
    cnt += len(A) # 남은 글자 수 만큼 1회 증가
    print(f'#{tc+1} {cnt}')