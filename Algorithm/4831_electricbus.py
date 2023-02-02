'''
전기버스
한번 충전하면 K 만큼 이동
충전소는 총 M 개
종점은 N번 정류장
출발할 때 풀충전 (충전횟수 포함 x)

입력 : 테스트 케이스, K N M, 충전소 위치(M개)
출력 : 몇 번 충전해야 도착할 수 있는지, 도착 못하면 0

버스가 0에서 N까지 가기 위해
현재 위치에서 가장 가까운 충전소와 두번째로 가까운 충전소를 구간으로 잡고
    현재 위치 + K 가 N 이상이면 종료
    그렇지 않다면 아래 반복
        현재 위치 + K 가 다음 충전소를 넘어간다면
            그 다음 구간으로 넘긴다
        현재 위치 + K 가 다음 충전소까지라면
            위치값을 다음 충전소로 변환 후 충전 +1
        현재 위치 + K 가 첫 충전소와 다음 충전소 사이에 멈추면
            위치값을 첫 충전소로 변환 후 충전 +1
        현재 위치 + K 가 첫 충전소 전에 멈추면
            0 반환
테스트 케이스와 충전횟수 출력
'''
total_case = int(input())
case = 0
while case < total_case: # 테스트 케이스만큼 반복
    K, N, M = map(int,input().split())
    M_num = list(map(int,input().split()))
    M_num.append(N) # 구간 인덱스를 위해 임의의 큰 값(목적지) 추가
    bus_position = 0; choongjeon = 0 # 버스 위치와 충전횟수를 셀 변수들 선언
    for i in range(len(M_num)-1): # 임의값 추가했으니까 -1
        if bus_position + K >= N: # 목적지를 넘어간다면 break
            break
        if bus_position + K > M_num[i+1]:
            pass
            # 두번째로 가까운 충전소를 넘어간다면 pass
        elif bus_position + K == M_num[i+1]:
            bus_position = M_num[i+1]
            choongjeon += 1
            # 두번째 충전소까지 갈 수 있다면 그 위치값을 가지고 충전 +1
        elif bus_position + K >= M_num[i] and bus_position + K < M_num[i+1]:
            bus_position = M_num[i]
            choongjeon += 1
            # 첫 충전소와 두번째 충전소 사이까지 갈 수 있다면
            # 첫 충전소의 위치값을 가지고 충전 +1
        else:
            choongjeon = 0
            # 첫 충전소도 못가면 0 출력해야하므로 충전 = 0
    print(f'#{case+1} {choongjeon}') # 출력

    case += 1

