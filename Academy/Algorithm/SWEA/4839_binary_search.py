'''
입력값 : 테스트 케이스 수 / 전체 쪽수 , A가 찾을 쪽, B가 찾을 쪽
출력값 : # 테케 , 더 빨리 찾은 애, 비기면 0
'''
test_case = int(input())
for i in range(test_case):
    P, A, B = map(int,input().split())
    A_cnt = 0; B_cnt = 0

    start = 1
    end = P
    while start <= end:
        middle = (start + end) // 2
        if middle == A:
            break
        elif middle > A:
            A_cnt += 1
            end = middle
        else: # middle < A
            A_cnt += 1
            start = middle

    start = 1
    end = P
    while start <= end:
        middle = (start + end) // 2
        if middle == B:
            break
        elif middle > B:
            B_cnt += 1
            end = middle
        else:
            B_cnt += 1
            start = middle

    if A_cnt < B_cnt:
        print(f'#{i + 1} A')
    elif B_cnt < A_cnt:
        print(f'#{i + 1} B')
    else:
        print(f'#{i + 1} 0')

