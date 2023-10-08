'''
입력받은 테스트 케이스의 수 만큼 아래를 반복한다
    array 입력받음 (length : N)
    첫 원소의 값을 기준으로
        값보다 크면 max
        값보다 작으면 min
    최종적으로 max - min 을 출력
'''
T = int(input()) # 테스트 케이스의 수
test_number = 1 # 테스트 개수를 셀 counter
for _ in range(T) : # 테스트 케이스 만큼
    N = int(input())
    array = list(map(int, input().split()))
    maximum = int(array[0])
    minimum = int(array[0]) # 첫 원소의 값을 기준으로 잡음
    for i in range(1,N) :
        if array[i] > maximum : # 값보다 크면 max
            maximum = array[i]
        elif array[i] < minimum : # 값보다 작으면 min
            minimum = array[i]
        else : # 그 외 경우 pass
            pass
    answer = maximum - minimum
    print(f'#{test_number} {answer}') # max - min 을 출력
    test_number += 1 # 테스트 케이스의 횟수 증가
