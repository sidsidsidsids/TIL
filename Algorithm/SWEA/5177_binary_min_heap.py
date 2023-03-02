def enQ(n):
    global last
    last += 1  # 완전이진트리의 마지막 정점을 추가
    heap[last] = n  # 마지막 정점에 저장
    c = last  # 부모가 있고, 부모 < 자식인지 조건 검사
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p  # 옮긴 자리에서의 부모와 비교하기 위해
        p = c // 2
    return

test_case = int(input())
for tc in range(1,test_case+1):
    N = int(input())
    heap = [0] * (N+1) 
    last = 0  # 완전이진트리의 마지막 정점 번호

    numbers = list(map(int,input().split()))
    for n in numbers:
        enQ(n)

    answer = 0
    while N//2 > 0:
        answer += heap[N//2]
        N //= 2

    print(f'#{tc} {answer}')
