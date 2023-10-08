'''
일반 버스 : A~B 모두
급행 버스 : A가 홀수면 A와 B사이 모든 홀수,
          A가 짝수면 A와 B사이 모든 짝수
광역 버스 : A가 홀수면 A와 B사이 3의 배수이면서 10의 배수가 아닌
          A가 짝수면 A와 B사이 모든 4의 배수

최대 몇개의 노선이 같은 정류장에서 정차?(같은 값?)
리스트들을 만들어 비교
2 3 4 5
3 5 7 9 10
2 4 8 9
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    total_lists = []; end_value = []
    for _ in range(N):
        bus_route = []
        bus_type, bus_start, bus_end = map(int,input().split())

        # 일반 버스
        if bus_type == 1:
            for i in range(bus_start,bus_end+1):
                bus_route.append(i)
        # 급행 버스
        elif bus_type == 2:
            bus_route.append(bus_start)
            if bus_start % 2 == 0 : # 짝수일 때 모든 짝수
                for i in range(bus_start+1, bus_end):
                    if i % 2 == 0 :
                        bus_route.append(i)
            else : # 홀수일 때 모든 홀수
                for i in range(bus_start + 1, bus_end):
                    if i % 2 != 0:
                        bus_route.append(i)
            bus_route.append(bus_end)
        # 광역 버스
        else:
            bus_route.append(bus_start)
            if bus_start % 2 == 0:  # 짝수일 때 모든 4의 배수
                for i in range(bus_start+1, bus_end):
                    if i % 4 == 0 :
                        bus_route.append(i)
            else : # 홀수일 때 3의 배수면서 10의 배수가 아닌 수
                for i in range(bus_start + 1, bus_end):
                    if i % 10 != 0 and i % 3 == 0:
                        bus_route.append(i)
            bus_route.append(bus_end)

        total_lists.append(bus_route)
        end_value.append(bus_end)

    end_value = max(end_value)
    cnt_lst = [0] * end_value
    for i in range(1,end_value+1):
        for j in range(len(total_lists)):
            if i in total_lists[j]:
                cnt_lst[i-1] += 1
    ans = max(cnt_lst)

    print(f'#{test_case}', ans)


