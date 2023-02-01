'''
테스트 케이스 횟수 입력
사각형 크기 입력
박스들의 높이 입력

#한 줄을 기준으로 그 줄보다 높은 줄을 만날 때 까지의 거리(횟수)를 계산
#이 값을 저장하여 값들중 가장 큰 값을 출력 -> 반례 : test case 3

오른쪽 벽까지의 거리를 계산
가로막는 높이의 상자 횟수만큼 거리 합산 X

'''

T = int(input()) # 테스트 케이스 수 입력받음
count = 0 # 순환문 탈출을 위한 변수 선언
while count < T: # 테스트 케이스 횟수를 채울 만큼 반복
    N = int(input()) # 오른쪽 벽까지의 거리 입력
    boxes = list(map(int,input().split())) # 상자들의 높이 입력
    distance_list=[] # 거리값들을 저장할 리스트 선언
    for i in range(N): # 각 박스묶음들 마다
        distance = 0 # 거리를 잴 변수 선언
        for j in range(i+1,N): # 지정한 박스보다 우측에 있는 박스묶음들
            if boxes[i] > boxes[j]: # 지정한 박스가 더 높다면
                distance += 1 # 거리 + 1
            else: # 오른쪽에 있는 박스묶음이 더 높거나 같다면
                pass # 거리에 1을 더하지 않음
        distance_list.append(distance) # 거리들을 리스트에 추가
    answer = 0 # 가장 높은 값을 저장할 정답 변수 선언
    for dist in distance_list: # 리스트 내 값들을 순환
        if dist > answer:
            answer = dist # dist가 answer보다 클 때마다 값 갱신
    print(f'#{count+1} {answer}') # 출력
    count += 1 # 순환을 위한 변수 +1