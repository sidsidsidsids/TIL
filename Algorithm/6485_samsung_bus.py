'''
입력 : 테스트 케이스 수 T, 각 테스트 횟수 N, N개의 두 정수 Ai Bi, P, P개의 정수 Cj

삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고, Bi이하인
모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지
'''
total_case = int(input())
case = 0
while case < total_case:
    buses = int(input())
    A = []; B = []
    for i in range(buses):
        Ai, Bi = map(int,input().split())
        A.append(Ai)
        B.append(Bi)
    P = int(input())
    bus_stop = [0]*P
    C = []
    for i in range(P):
        Ci = int(input())
        C.append(Ci)
    for i in range(buses):
        for j in range(A[i]-1,B[i]):
            bus_stop[j] += 1
    # answer = ''
    # for num in bus_stop:
    #     answer += f' {int(num)}'
    print(f'#{case+1}', *bus_stop)
    case += 1
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0]*5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1
            
    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])
    print(f'#{test_case}', *alst)
'''