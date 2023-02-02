'''
 i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
 초기값 : 모든 상자 전부 0

 입력 : 테스트 케이스, N(상자 개수) Q(반복 회수), L(eft) R(ight)
 출력 : #테스트 번호, 상자들 숫자
'''
total_case = int(input())
case = 0
while case < total_case:
    N, Q = map(int,input().split())
    boxes = [0] * N
    for i in range(Q):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            boxes[j] = i+1
    answer = ''
    for num in boxes:
        answer += f' {num}'
    print(f'#{case+1}{answer}')
    case += 1
