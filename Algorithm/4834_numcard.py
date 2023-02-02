'''
0부터 9까지 적힌 카드 (10 종류)
카드들을 세서 가장 많은 것과 그 장수를 출력
count sort 하던거 응용
'''

total_case = int(input())
case = 0
while case < total_case:
    card_amount = int(input()) # 카드 장수 N
    cards = list(map(int,str(input()))) # N개의 숫자
    count_list = [0] * 10 # 숫자를 셀 카운트 리스트
    for i in cards:
        count_list[i] += 1 # 입력받은 카드 숫자 세기
    max_value = count_list[::-1].index(max(count_list))
    # 최댓값 중복시 더 높은 숫자를 출력해야 하므로 리스트 뒤에서 부터 max값을 찾도록
    max_value = 9-max_value
    # 뒤에서 세서 인덱스 값이 거꾸로 되있으므로 다시 원래대로
    max_count = max(count_list) # 최대값의 개수
    print(f'#{case+1} {max_value} {max_count}')

    case += 1
