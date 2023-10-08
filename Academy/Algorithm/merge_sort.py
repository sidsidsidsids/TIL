
def msort(s, e):
    global cnt
    if s + 1 == e:
        return
    # else: if에 return 있으니까 생략
    m = (s+e) // 2
    # 문제 조건에 맞는 범위 설정
    msort(s, m)
    msort(m, e)

    # merge()
    k = 0
    l, r = s, m # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l < m and r < e: # 왼쪽 오른쪽 둘 다 남은 게 있을 때
        if l < m and r < e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
    if l >= m: # 왼쪽에 남은 원소가 더 이상 없다
        while r < e: # 오른쪽거 다 넘기기
            tmp[k] = arr[r]
            r += 1
            k += 1
    else: # 왼쪽에 남은 원소가 있다. 오른쪽은 없다
        while l < m: # 왼쪽거 다 넘기기, cnt + 1
            tmp[k] = arr[l]
            l += 1
            k += 1
        cnt += 1

    # 완성한 temp를 array에 반영
    i = 0
    while i < k:
        arr[s + i] = tmp[i]
        i += 1
    return # 수정된 array를 반영

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N
    cnt = 0

    msort(0,N)
    print(f'#{t} {arr[N//2]} {cnt}')