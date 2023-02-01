'''
테스트 케이스 수 만큼 아래를 반복
    array(길이가 N)와 구간(길이가 M)을 받음
    첫 구간의 합을 기준으로
        그 다음 구간이 더 크면 maximum
        그 다음 구간이 더 작으면 minimum
    maximum - minimum 값을 출력
'''
T = int(input()) # 테스트 케이스의 수
test_number = 1 # 테스트 개수를 셀 counter
for _ in range(T): # 테스트 케이스 수 만큼 아래를 반복
    N, M = map(int,input().split())
    array = list(map(int,input().split())) # array(길이가 N)와 구간(길이가 M)을 받음
    maximum = 0 ; minimum = 0
    for i in range(M):
        maximum += array[i]
        minimum += array[i] # 첫 구간의 합을 기준으로
    for i in range(1,N-M+1):
        if sum(array[i:i+M]) > maximum:
            maximum = sum(array[i:i+M]) # 그 다음 구간이 더 크면 maximum
        elif sum(array[i:i+M]) < minimum:
            minimum = sum(array[i:i+M]) # 그 다음 구간이 더 작으면 minimum
        else:
            pass # 그 외의 경우 pass
    answer = maximum - minimum # 답안
    print(f'#{test_number} {answer}')  # max - min 을 출력
    test_number += 1  # 테스트 케이스의 횟수 증가
