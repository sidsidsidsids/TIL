T = int(input())
for tc in range(1, T+1):
    n = int(input())
    carrots = list(map(int,input().split()))

    minV = 1000
    for i in range(n-2):
        for j in range(i+1,n-1):
            if carrots[i] != carrots[i+1] and carrots[j] != carrots[j+1]:
                A = i + 1
                B = j - i
                C = n - j - 1
                if min(A,B,C) != 0:
                    if A <= n//2 and B <= n//2 and C <= n//2:
                        if minV > max(A,B,C) - min(A,B,C):
                            minV = max(A,B,C) - min(A,B,C)
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')
'''
    # 오름차수 정렬
    carrots.sort()

    minV = 1000
    for i in range(n-2): # 소 박스
        for j in range(i+1,n-1): # 중 박스
            if carrots[i] != carrots[i+1] and carrots[j] != carrots[j+1]:
                # 같은 크기가 다른 박스에 들어가는 경우 제외하기
                A = i + 1
                B = j - i
                C = n - 1 - j
                if A*B*C != 0: # 크기가 0인 박스 있는 경우 제외
                    if A <= n//2 and B <= n//2 and C <= n//2:
                        if minV > max(A,B,C) - min(A,B,C):
                            minV = max(A,B,C) - min(A,B,C)
    if minV != 1000:
        print(f'#{tc} {minV}')
    else:
        print(f'#{tc} -1')
'''
'''
    size = [0] * 31 # 당근 크기가 1~30 이므로
    for c in carrots:
        size[c] += 1

    minV = 1000
    for i in range(31-2):
        for j in range(i+1,31-1):
            A = sum(size[:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:])
            if A*B*C != 0: # 크기가 0인 박스 있는 경우 제외
                if A <= n//2 and B <= n//2 and C <= n//2:
                    if minV > max(A,B,C) - min(A,B,C):
                        minV = max(A,B,C) - min(A,B,C)

    if minV != 1000:
        print(f'#{tc} {minV}')
    else:
        print(f'#{tc} -1')
'''
