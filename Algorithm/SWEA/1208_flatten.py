'''
덤프 횟수와 상자들의 층 입력

가장 높은 상자 -= 1, 가장 낮은 상자 += 1
위 행동을 취할 때 마다 덤프 +1

제한된 덤프 횟수 이후 가장 높은 상자와 낮은 상자의 층 차이 출력
단 그 전에 평탄화(max - min <= 1)가 된다면 그 때의 차이 출력
'''

count = 0
while count < 10 : # 10개의 테스트 케이스를 돌리기 위한 반복문
    dump_num = int(input()) # 덤프 횟수
    boxes = list(map(int,input().split())) # 박스들의 층
    dump = 0
    while dump < dump_num: # 덤프 횟수만큼 반복
        boxes[boxes.index(max(boxes))] -= 1 # 최댓값 -1
        boxes[boxes.index(min(boxes))] += 1 # 최솟값 +1
        dump += 1 # 덤프 1회 추가
        if max(boxes) - min(boxes) <= 1:
            break # 입력받은 횟수 이전에 평탄화가 되면 반복문 종료
    print(f'#{count+1} {max(boxes)-min(boxes)}')
    count += 1